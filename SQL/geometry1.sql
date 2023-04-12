SELECT
    CASE
        WHEN geometry::STGeomFromWKB(t.SHAPE.STAsBinary(), 4326).STIsValid() = 1
        THEN geometry::STGeomFromWKB(t.SHAPE.STAsBinary(), 4326 ).STCentroid().STY
        ELSE NULL
    END TRN_CENTROID_LATITUDE,
    CASE
        WHEN geometry::STGeomFromWKB(t.SHAPE.STAsBinary(), 4326).STIsValid() = 1
        THEN geometry::STGeomFromWKB(t.SHAPE.STAsBinary(), 4326 ).STCentroid().STX
        ELSE NULL
    END TRN_CENTROID_LONGITUDE,
    CASE
        WHEN t.SHAPE IS NULL
        THEN 'NULL'
        ELSE
            CASE
                WHEN geometry::STGeomFromWKB(t.SHAPE.STAsBinary(), 4326).STIsValid() = 1
                THEN 'VALID'
                ELSE 'INVALID'
            END
    END GEOMETRY_IS_VALID
FROM POLYGON_TABLE t