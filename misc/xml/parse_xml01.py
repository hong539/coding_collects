import xml.etree.ElementTree as ET

def parse_pom(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Define the namespaces used in the pom.xml file
    namespaces = {
        'mvn': 'http://maven.apache.org/POM/4.0.0'
    }
    
    # Extract basic information
    group_id = root.find('mvn:groupId', namespaces)
    artifact_id = root.find('mvn:artifactId', namespaces)
    version = root.find('mvn:version', namespaces)
    
    # Print basic information
    print("Group ID:", group_id.text if group_id is not None else "Not found")
    print("Artifact ID:", artifact_id.text if artifact_id is not None else "Not found")
    print("Version:", version.text if version is not None else "Not found")
    
    # Extract dependencies
    dependencies = root.find('mvn:dependencies', namespaces)
    if dependencies is not None:
        for dependency in dependencies.findall('mvn:dependency', namespaces):
            dep_group_id = dependency.find('mvn:groupId', namespaces)
            dep_artifact_id = dependency.find('mvn:artifactId', namespaces)
            dep_version = dependency.find('mvn:version', namespaces)
            
            print("\nDependency:")
            print("  Group ID:", dep_group_id.text if dep_group_id is not None else "Not found")
            print("  Artifact ID:", dep_artifact_id.text if dep_artifact_id is not None else "Not found")
            print("  Version:", dep_version.text if dep_version is not None else "Not found")

# Example usage
parse_pom('path/to/your/pom.xml')