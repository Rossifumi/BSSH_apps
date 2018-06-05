function launchSpec(dataProvider)
{
    var samples = dataProvider.GetProperty('Input.sample-id');
    var outputProject = dataProvider.GetProperty("Input.project-id");
    var dataGenomeFolder = dataProvider.GetProperty("Input.DATA-GenomeFolder");
    var bcPattern = dataProvider.GetProperty("Input.bc-pattern");
    
    var ret = { nodes: [] };
    for (var i = 0; i < samples.length; i++) {
        var sample = samples[i];
        ret.nodes.push({
            commandLine: [ "/usr/bin/python", 
                        "/umi-tools-app-fastq.py",
                        "/data/input",
                        "/data/output",
                        "/data/scratch",
                        "/data/logs"
                    ],
            containerImageId: "docker.cnn1.sh.basespace.illumina.com.cn/jjxu/umitools_py",
            Options: [ "bsfs.enabled=true" ],
            Properties: {
                "Input.Samples": [sample],
                "Output.Projects": [outputProject],
                "Input.sample-id": sample,
                "Input.project-id": outputProject,
                "Input.DATA-GenomeFolder": dataGenomeFolder,
                "Input.bc-pattern": bcPattern
            }
        });
    }
    return ret;
}

/*
function launchSpec(dataProvider)
{
    var ret = {
        commandLine: [ "/usr/bin/python", 
                        "/umi-tools-app-fastq.py",
                        "/data/input",
                        "/data/output",
                        "/data/scratch",
                        "/data/logs"
                    ],
        containerImageId: "docker.cnn1.sh.basespace.illumina.com.cn/jjxu/umitools_py",
        Options: [ "bsfs.enabled=true" ]
    };
    return ret;
}
*/

// example multi-node launch spec
/*
function launchSpec(dataProvider)
{
    var ret = {
        nodes: []
    };
    
    ret.nodes.push({
        appSessionName: "Hello World 1",
        commandLine: [ "cat", "/illumina.txt" ],
        containerImageId: "basespace/demo",
        Options: [ "bsfs.enabled=true" ]
    });
    
    ret.nodes.push({
        appSessionName: "Hello World 2",
        commandLine: [ "cat", "/illumina.txt" ],
        containerImageId: "basespace/demo",
        Options: [ "bsfs.enabled=true" ]
    });
    
    return ret;
}
*/

/* 
function billingSpec(dataProvider) {
    return [
    {
        "Id" : "insert product ID here",
        "Quantity": 1.0
    }];
}
*/