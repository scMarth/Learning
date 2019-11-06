<?php
    // ini_set('display_errors', 1);
    // ini_set('display_startup_errors', 1);
    ini_set('memory_limit', '-1');
    date_default_timezone_set('America/Los_Angeles');

    // returns the number of hours between two (int) Unix timestamps
    function hoursBetweenTimestamps($start, $end){
        $delta = $end - $start;
        $hours = $delta / 3600;
        return $hours;
    }

    // Converts a Unix timestamp to a human readable string in the local timezone.
    function timestampToDateStr($timestamp){
        $lt = localtime($timestamp, true);
        $string = ($lt['tm_mon']+1) . '/' . $lt['tm_mday'] . '/' . ($lt['tm_year']+1900);
        return $string;
    }

    function dateCompare($a, $b){
        $t1 = strtotime($a['DateStart']);
        $t2 = strtotime($b['DateStart']);
        return $t1 - $t2;
    }

    function constructDataset(&$datasets, $keys, $field, &$hash){
        $prevDate = '';

        for ($i=0; $i<count($keys); $i++){
            $key = $keys[$i];
            $datasets[$key] = array();
        }

        usort($hash, 'dateCompare');

        foreach ($hash as $record){

            $dateStart = $record['DateStart'];
            $projectType = $record[$field];

            if ($dateStart == $prevDate){
                foreach ($datasets as $key=>&$val){
                    if ($key == $projectType){
                        $val[count($val) - 1]++;
                    }
                }
            }else{
                foreach ($datasets as $key=>&$val){
                    $prevDate = $dateStart;
                    if ($key == 'dates'){
                        array_push($val, $dateStart);
                    }elseif ($key == $projectType) {
                        if (count($val) == 0){
                            array_push($val, 1);
                        }else{
                            $lastVal = array_values(array_slice($val, -1))[0];
                            array_push($val, $lastVal + 1);
                        }
                    }else{
                        if (count($val) == 0){
                            array_push($val, 0);
                        }else{
                            $lastVal = array_values(array_slice($val, -1))[0];
                            array_push($val, $lastVal);
                        }
                    }
                }
            }
        }
    }

    /*
    For every key in $totals, store $totals[key] / $counts[key] in
    $averages[key]
    */
    function calculateAverages(&$averages, $counts, $totals){
        foreach ($totals as $key=>&$val){
            $avg = round($totals[$key]/$counts[$key], 3);
            $averages[$key] = $avg;
        }
    }

    $strJsonFileContents = file_get_contents('./json/311-data.json');

    $array = json_decode($strJsonFileContents, true);

    $numRecords = count($array);

    $departmentFreq = array();
    $districtFreq = array();
    $typenameFreq = array();
    $originFreq = array();

    # average requests per department
    $departmentHours = array(); # mapping departments to total Hours
    $numDepartmentRecordsWithHours = array(); # mapping number of records with department and Hours
    $avgDepartmentHours = array(); # mapping  departments to average Hours

    # average requests per district
    $districtHours = array();
    $numDistrictRecordsWithHours = array();
    $avgDistrictHours = array();

    # average requests per typename
    $typenameHours = array();
    $numTypenameRecordsWithHours = array();
    $avgTypenameHours = array();

    # average requests per origin
    $originHours = array();
    $numOriginRecordsWithHours = array();
    $avgOriginHours = array();

    # for departments timeline
    $departmentHash = array();
    $departmentTypes = array();
    $departmentDatasets = array('dates'=>array());

    # for districts timeline
    $districtHash = array();
    $districtTypes = array();
    $districtDatasets = array('dates'=>array());

    # for typename timeline
    $typenameHash = array();
    $typenameTypes = array();
    $typenameDatasets = array('dates'=>array());

    # for origin timeline
    $originHash = array();
    $originTypes = array();
    $originDatasets = array('dates'=>array());


    # request code counts
    $openRequests = 0;
    $closedRequests = 0;
    $inProgressRequests = 0;
    $onHoldRequests = 0;

    for ($i = 0; $i<$numRecords; $i++){
    // for ($i = 0; $i<10; $i++){
    //     var_dump($array[$i]['fields']);
    //     echo '<br><br>';

        $department = $array[$i]['fields']['dept'];
        $district = $array[$i]['fields']['district'];
        $typename = $array[$i]['fields']['typename'];
        $record = $array[$i]['fields'];
        $tsClosed = (int)$array[$i]['fields']['dateclosedunix'];
        $tsAdded = (int)$array[$i]['fields']['adddateunix'];
        $id = $array[$i]['fields']['id'];
        $hoursBetween = null;
        $requestStatus = $array[$i]['fields']['status'];
        $origin = $array[$i]['fields']['origin'];

        # keep a count for each request status type
        switch ($requestStatus){
            case 0:
                $openRequests++;
                break;
            case 1:
                $closedRequests++;
                break;
            case 3:
                $inProgressRequests++;
                break;
            case 4:
                $onHoldRequests++;
                break;
            default:
                echo 'Unknown Request Type<br>';
        }

        if ($tsClosed && $tsAdded){
            $hoursBetween = hoursBetweenTimestamps($tsAdded, $tsClosed);
        }

        if ($department){
            if (!array_key_exists($department, $departmentFreq)){
                $departmentFreq[$department] = 0;
            }
            $departmentFreq[$department]++;
        }

        if ($district){
            if (!array_key_exists($district, $districtFreq)){
                $districtFreq[$district] = 0;
            }
            $districtFreq[$district]++;
        }

        if ($typename){
            if (!array_key_exists($typename, $typenameFreq)){
                $typenameFreq[$typename] = 0;
            }
            $typenameFreq[$typename]++;
        }

        if ($origin){
            if (!array_key_exists($origin, $originFreq)){
                $originFreq[$origin] = 0;
            }
            $originFreq[$origin]++;
        }

        # get information for departments timeline
        if ($tsAdded && $department){
            array_push($departmentHash, array('id'=>$id, 'DateStart'=>timestampToDateStr($tsAdded), 'Department'=>$department));
            if (!in_array($department, $departmentTypes))
                array_push($departmentTypes, $department);
        }

        # get information for district timeline
        if ($tsAdded && $district){
            array_push($districtHash, array('id'=>$id, 'DateStart'=>timestampToDateStr($tsAdded), 'District'=>$district));
            if (!in_array($district, $districtTypes))
                array_push($districtTypes, $district);
        }

        # get information for typename timeline
        if ($tsAdded && $typename){
            array_push($typenameHash, array('id'=>$id, 'DateStart'=>timestampToDateStr($tsAdded), 'Typename'=>$typename));
            if (!in_array($typename, $typenameTypes))
                array_push($typenameTypes, $typename);
        }

        # get information for origin timeline
        if ($tsAdded && $origin){
            array_push($originHash, array('id'=>$id, 'DateStart'=>timestampToDateStr($tsAdded), 'Origin'=>$origin));
            if (!in_array($origin, $originTypes))
                array_push($originTypes, $origin);
        }

        if ($department && $tsClosed && $tsAdded){
            if (!array_key_exists($department, $departmentHours)){
                $departmentHours[$department] = 0;
            }
            if (!array_key_exists($department, $numDepartmentRecordsWithHours)){
                $numDepartmentRecordsWithHours[$department] = 0;
            }
            $departmentHours[$department] += $hoursBetween;
            $numDepartmentRecordsWithHours[$department]++;
        }

        if ($district && $tsClosed && $tsAdded){
            if (!array_key_exists($district, $districtHours)){
                $districtHours[$district] = 0;
            }
            if (!array_key_exists($district, $numDistrictRecordsWithHours)){
                $numDistrictRecordsWithHours[$district] = 0;
            }
            $districtHours[$district] += $hoursBetween;
            $numDistrictRecordsWithHours[$district]++;
        }

        if ($typename && $tsClosed && $tsAdded){
            if (!array_key_exists($typename, $typenameHours)){
                $typenameHours[$typename] = 0;
            }
            if (!array_key_exists($typename, $numTypenameRecordsWithHours)){
                $numTypenameRecordsWithHours[$typename] = 0;
            }
            $typenameHours[$typename] += $hoursBetween;
            $numTypenameRecordsWithHours[$typename]++;
        }

        if ($origin && $tsClosed && $tsAdded){
            if (!array_key_exists($origin, $originHours)){
                $originHours[$origin] = 0;
            }
            if (!array_key_exists($origin, $numOriginRecordsWithHours)){
                $numOriginRecordsWithHours[$origin] = 0;
            }
            $originHours[$origin] += $hoursBetween;
            $numOriginRecordsWithHours[$origin]++;
        }


    }

    calculateAverages($avgDepartmentHours, $numDepartmentRecordsWithHours, $departmentHours);
    calculateAverages($avgDistrictHours, $numDistrictRecordsWithHours, $districtHours);
    calculateAverages($avgTypenameHours, $numTypenameRecordsWithHours, $typenameHours);
    calculateAverages($avgOriginHours, $numOriginRecordsWithHours, $originHours);

    // echo '<br><br>';
    // var_dump($avgDepartmentHours);
    // echo '<br><br>';
    // var_dump($numDepartmentRecordsWithHours);
    // echo '<br><br>';
    // var_dump($departmentHours);

    $requestStatusFreq = array(
        'Open'          => $openRequests,
        'Closed'        => $closedRequests,
        'In-Progress'   => $inProgressRequests,
        'On-Hold'       => $onHoldRequests
    );

    constructDataset($departmentDatasets, $departmentTypes, 'Department', $departmentHash);
    constructDataset($districtDatasets, $districtTypes, 'District', $districtHash);
    constructDataset($typenameDatasets, $typenameTypes, 'Typename', $typenameHash);
    constructDataset($originDatasets, $originTypes, 'Origin', $originHash);

    # sort arrays
    foreach (array(&$departmentFreq, &$departmentHours, &$avgDepartmentHours, &$departmentDatasets,
        &$districtFreq, &$districtHours, &$avgDistrictHours, &$districtDatasets,
        &$typenameFreq, &$typenameHours, &$avgTypenameHours, &$typenameDatasets,
        &$originFreq, &$originHours, &$avgOriginHours, &$originDatasets) as &$arr){
        ksort($arr);
    }

    unset($arr);

?>