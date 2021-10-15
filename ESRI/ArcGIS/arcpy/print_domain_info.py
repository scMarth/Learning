import arcpy, json, os, sys

fc = r"D:\TEST_CONNECTION\TEST.sde"

domain_data = arcpy.da.ListDomains(fc)
print(domain_data)

for domain in domain_data:
    print('domain name: {}'.format(domain.name))

    if domain.domainType == 'CodedValue':
        coded_values = domain.codedValues
        for val, desc in coded_values.items():
            print('{0} : {1}'.format(val, desc))
    elif domain.domainType == 'Range':
        print('Min: {0}'.format(domain.range[0]))
        print('Max: {0}'.format(domain.range[1]))

    print('')