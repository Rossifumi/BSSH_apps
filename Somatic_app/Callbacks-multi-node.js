function launchSpec(dataProvider)
{
    var samples = dataProvider.GetProperty('Input.app-result-id');
    var outputProject = dataProvider.GetProperty("Input.project-id");
    
    var hygeaParams = dataProvider.GetProperty("Input.hygea-params");
    var stitcherParams = dataProvider.GetProperty("Input.stitcher-params");
    var piscesParams = dataProvider.GetProperty("Input.pisces-params");
    
    var ret = { nodes: [] };
    for (var i = 0; i < samples.length; i++) {
        var sample = samples[i];
        ret.nodes.push({
            commandLine: [ "/usr/bin/python", 
                            "/somatic_app.py",
                            "/data/input",
                            "/data/output",
                            "/data/scratch",
                            "/data/logs"
                        ],
            containerImageId: "docker.illumina.com/jjxu/somatic_app",
            Options: [ "bsfs.enabled=true" ],
            Properties: {
                "Input.AppResults": [sample.ParentAppResult],
                //"Input.Files": [bam],
                "Output.Projects": [outputProject],
                "Input.app-result-id": sample,
                "Input.project-id": outputProject,
                "Input.hygea-params": hygeaParams,
                "Input.stitcher-params": stitcherParams,
                "Input.pisces-params": piscesParams
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
                        "/somatic_app.py",
                        "/data/input",
                        "/data/output",
                        "/data/scratch",
                        "/data/logs"
                    ],
        containerImageId: "docker.illumina.com/jjxu/somatic_app",
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