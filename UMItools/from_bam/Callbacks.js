function launchSpec(dataProvider)
{
    var ret = {
        commandLine: [ "/usr/local/python2.7.12/bin/python", 
                        "/umi-tools-app.py",
                        "/data/input",
                        "/data/output",
                        "/data/scratch",
                        "/data/logs"
                    ],
        containerImageId: "docker.illumina.com/jjxu/umitools_from_bam",
        Options: [ "bsfs.enabled=true" ]
    };
    return ret;
}

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