/* 
    getMeta.js

    A script used to query metadata from a particular instance of a Google Cloud Compute Engine. If no specific property
    is requested, return all.

    args - 
    0: Instance metadata url - Ex: http://metadata.google.internal/computeMetadata/v1/instance/disks/?recursive=true
    1: (optional) Desired propery - Ex: 'deviceName'

    Can be invoked via the command line: 
    node getMeta.js http://metadata.google.internal/computeMetadata/v1/instance/disks/?recursive=true deviceName
*/
const args = process.argv.slice(2);

const getMetaData = async (url, desiredProperty) => {
    if (!url) {
        return "Please provide instance metadata URL as the first argument"
    }
    try {
        const response = await fetch(url, {headers: {'Metadata-Flavor': 'Google'}})
        const json = await response.json()
        if (args.length > 1) {
            if (json[0].hasOwnProperty(desiredProperty)) {
                return {[desiredProperty]: json[0][desiredProperty]}
            } else {
                return "instance does not contain property"
            }
        } else {
            return json[0]   
        }
    } catch (e) {
        return ["Looks like there was an error. Make sure you're passing the instance metadata URL as the first argument." ,e]
    }
}

[url, desiredProperty] = args;

getMetaData(url, desiredProperty).then(res => console.log(res))