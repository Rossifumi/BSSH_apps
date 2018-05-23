function launchSpec(dataProvider)
{
    //var appResults = dataProvider.GetProperty("Input.AppResults");
    
    var bams = dataProvider.GetProperty("Input.app-result-id");
    var outputProject = dataProvider.GetProperty("Input.project-id");
    
    var otherParams = dataProvider.GetProperty("Input.other-params");
    
    var ret = { nodes: [] };
    
    for (var i = 0; i < bams.length; i++) {
        var bam = bams[i];
        
        ret.nodes.push({
            commandLine: [ "/usr/bin/python", 
                            "/pisces527_app.py",
                            "/data/input",
                            "/data/output",
                            "/data/scratch",
                            "/data/logs"
                        ],
            containerImageId: "docker.illumina.com/jjxu/pisces527",
            Options: [ "bsfs.enabled=true" ],
            Properties: {
                //"Input.AppResults": [appResults],
                "Input.AppResults": [bam.ParentAppResult],
                "Input.Files": [bam],
                "Output.Projects": [outputProject],
                "Input.app-result-id": bam,
                "Input.project-id": outputProject,
                "Input.other-params": otherParams
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
                        "/pisces527_app.py",
                        "/data/input",
                        "/data/output",
                        "/data/scratch",
                        "/data/logs"
                    ],
        containerImageId: "docker.illumina.com/jjxu/pisces527",
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