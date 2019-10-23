<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>311 Alerts (QScend)</title>
    <link rel='icon' href='images/SalinasLogoTagline.png'>
    <link rel='stylesheet' href='./css/styles.css'>

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

        // for ($i = 0; $i<$numRecords; $i++){
        for ($i = 0; $i<$numRecords; $i++){
            $department = $array[$i]['fields']['dept'];
            $district = $array[$i]['fields']['district'];
            $typename = $array[$i]['fields']['typename'];
            $record = $array[$i]['fields'];
            $tsClosed = (int)$array[$i]['fields']['dateclosedunix'];
            $tsAdded = (int)$array[$i]['fields']['adddateunix'];
            $id = $array[$i]['fields']['id'];
            $hoursBetween = null;

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
        }

        calculateAverages($avgDepartmentHours, $numDepartmentRecordsWithHours, $departmentHours);
        calculateAverages($avgDistrictHours, $numDistrictRecordsWithHours, $districtHours);
        calculateAverages($avgTypenameHours, $numTypenameRecordsWithHours, $typenameHours);

        // echo '<br><br>';
        // var_dump($avgDepartmentHours);
        // echo '<br><br>';
        // var_dump($numDepartmentRecordsWithHours);
        // echo '<br><br>';
        // var_dump($departmentHours);

        constructDataset($departmentDatasets, $departmentTypes, 'Department', $departmentHash);
        constructDataset($districtDatasets, $districtTypes, 'District', $districtHash);
        constructDataset($typenameDatasets, $typenameTypes, 'Typename', $typenameHash);

        # sort arrays
        foreach (array(&$departmentFreq, &$departmentHours, &$avgDepartmentHours,
            &$districtFreq, &$districtHours, &$avgDistrictHours,
            &$typenameFreq, &$typenameHours, &$avgTypenameHours) as &$arr){
            ksort($arr);
        }

        unset($arr);

    ?>

    <script src='./lib/Chart.bundle.min.js'></script>
    <script src='./js/colorGenerator.js'></script>
    <script src='./js/utils.js'></script>
</head>
<body>
    <div id='site-header'>
        <div class='salinas-logo'>
            <a href='https://www.cityofsalinas.org/' target='_blank'>
                <img class='image-logo' src='images/SalinasLogoTagline.png'>
            </a>
        </div>
    </div>

    <div class="panels">
        <div class="panel">
            <div class="canvas-container">
                <canvas id="department-requests"></canvas>
            </div>
            <div class="canvas-container">
                <canvas id="department-hours"></canvas>
            </div>
            <div class="canvas-container">
                <canvas id="department-avg-hours"></canvas>
            </div>
            <div class="canvas-container">
                <canvas id="department-request-timeline"></canvas>
            </div>
        </div>
        <div class="panel">
            <div class="canvas-container">
                <canvas id="district-requests"></canvas>
            </div>
            <div class="canvas-container">
                <canvas id="district-hours"></canvas>
            </div>
            <div class="canvas-container">
                <canvas id="district-avg-hours"></canvas>
            </div>
            <div class="canvas-container">
                <canvas id="district-request-timeline"></canvas>
            </div>
        </div>
        </div>
            <div class="panel">
                <div class="canvas-container" style="height:2000px;">
                    <canvas id="typename-requests"></canvas>
                </div>
                <div class="canvas-container" style="height:2000px;">
                    <canvas id="typename-hours"></canvas>
                </div>
                <div class="canvas-container" style="height:2000px;">
                    <canvas id="typename-avg-hours"></canvas>
                </div>
                <div class="canvas-container" style="height:2000px;">
                    <canvas id="typename-request-timeline"></canvas>
                </div>
            </div>
        </div>

<script>
    generatePieChartFromPhpArray(
        <?php echo json_encode($departmentFreq) ?>,
        'Total number of requests per department',
        'department-requests',
        true
    );

    generatePieChartFromPhpArray(
        <?php echo json_encode($departmentHours) ?>,
        'Total request hours per department (incomplete requests excluded)',
        'department-hours',
        true
    );

    generateHorizontalBarChartFromPhpArray(
        <?php echo json_encode($avgDepartmentHours) ?>,
        'Average hours per request for each department (incomplete requests excluded)',
        'department-avg-hours',
        'hours',
        true
    );

    // department timeline
    generateLineChartFromPhpData(
        <?php echo json_encode($departmentDatasets) ?>,
        'Department requests over time',
        'department-request-timeline',
        'start date',
        '# requests',
        true
    );

    generatePieChartFromPhpArray(
        <?php echo json_encode($districtFreq) ?>,
        'Total number of requests per district',
        'district-requests',
        true
    );

    generatePieChartFromPhpArray(
        <?php echo json_encode($districtHours) ?>,
        'Total request hours per district (incomplete requests excluded)',
        'district-hours',
        true
    );

    generateHorizontalBarChartFromPhpArray(
        <?php echo json_encode($avgDistrictHours) ?>,
        'Average hours per request for each district (incomplete requests excluded)',
        'district-avg-hours',
        'hours',
        true
    );

    // district timeline
    generateLineChartFromPhpData(
        <?php echo json_encode($districtDatasets) ?>,
        'District requests over time',
        'district-request-timeline',
        'start date',
        '# requests',
        true
    );

    generateHorizontalBarChartFromPhpArray(
        <?php echo json_encode($typenameFreq) ?>,
        'Total number of requests per typename',
        'typename-requests',
        '# requests',
        false
    );

    generateHorizontalBarChartFromPhpArray(
        <?php echo json_encode($typenameHours) ?>,
        'Total request hours per typename (incomplete requests excluded)',
        'typename-hours',
        'hours',
        false
    );

    generateHorizontalBarChartFromPhpArray(
        <?php echo json_encode($avgTypenameHours) ?>,
        'Average hours per request for each typename (incomplete requests excluded)',
        'typename-avg-hours',
        'hours',
        false
    );

    // typename timeline
    generateLineChartFromPhpData(
        <?php echo json_encode($typenameDatasets) ?>,
        'Typename requests over time',
        'typename-request-timeline',
        'start date',
        '# requests',
        false
    );
</script>
</body>
</html>