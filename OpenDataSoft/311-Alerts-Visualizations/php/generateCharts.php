<script>
    generateDoughnutChartFromPhpArray(
        <?php echo json_encode($requestStatusFreq) ?>,
        'Request Status',
        'status-requests',
        true
    );

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

    generatePieChartFromPhpArray(
        <?php echo json_encode($originFreq) ?>,
        'Total number of requests per origin',
        'origin-requests',
        true
    );

    generatePieChartFromPhpArray(
        <?php echo json_encode($originHours) ?>,
        'Total request hours per origin (incomplete requests excluded)',
        'origin-hours',
        true
    );

    generateHorizontalBarChartFromPhpArray(
        <?php echo json_encode($avgOriginHours) ?>,
        'Average hours per request for each origin (incomplete requests excluded)',
        'origin-avg-hours',
        'hours',
        true
    );

    // department timeline
    generateLineChartFromPhpData(
        <?php echo json_encode($originDatasets) ?>,
        'Origin requests over time',
        'origin-request-timeline',
        'start date',
        '# requests',
        true
    );
</script>