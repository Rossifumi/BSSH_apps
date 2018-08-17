function launchSpec(dataProvider)
{
    var ret = {
        commandLine: [ "/root/miniconda2/bin/python", 
                        "/vcanbio_test_app.py",
                        "/data/input",
                        "/data/output",
                        "/data/scratch",
                        "/data/logs"
                    ],
        containerImageId: "docker.illumina.com/jjxu/vcanbio_show",
        Options: [ "bsfs.enabled=true" ]
    };
    return ret;
}

