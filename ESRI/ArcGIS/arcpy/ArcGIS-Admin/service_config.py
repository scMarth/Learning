import os

configs = [
    {
        'env_name' : 'DEV',
        'configs' : []
    },
    {
        'env_name' : 'TEST',
        'configs' : [
            {
                'folder_name' : 'RBA',
                'services' : {
                    'ReceiptByApplication' : {}
                }
            },
            {
                'folder_name' : os.environ['ATLAS_SERVICE_FOLDER'],
                'services' : {
                    'GEOGRAPHIES' : {
                        'provider' : 'ArcObjects11',
                        'minInstancesPerNode' : 1,
                        'maxInstancesPerNode' : 3,
                        'maxWaitTime' : 120,
                        'FeatureServerEnabled' : True,
                        'FeatureServerCapabilities' : 'Create,Query,Update,Uploads,Editing'
                    },
                    'OFFLINE' : {},
                    'OPERATIONAL' : {},
                    'REPORTING' : {},
                    'REVIEWED_BLOCKS' : {},
                    'SUPPORT' : {}
                }
            }
        ]
    },
    {
        'env_name' : 'UAT',
        'configs' : []
    },
    {
        'env_name' : 'STAGE',
        'configs' : []
    },
    {
        'env_name' : 'PROD',
        'configs' : []
    }
]


