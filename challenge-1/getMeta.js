const args = process.argv.slice(2);

const getMetaData = async () => {
    try {
        const response = await fetch("http://metadata.google.internal/computeMetadata/v1/instance/disks/?recursive=true", {headers: {'Metadata-Flavor': 'Google'}})
        const json = await response.json()
        if (args.length > 0) {
            const desiredProperty = args[0];
            if (json[0].hasOwnProperty(desiredProperty)) {
                return {[desiredProperty]: json[0][desiredProperty]}
            } else {
                return "instance does not contain property"
            }
        } else {
            return json[0]   
        }
    } catch (e) {
        return e
    }
}

getMetaData().then(res => console.log(res))