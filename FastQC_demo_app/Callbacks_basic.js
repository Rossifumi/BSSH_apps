function launchSpec(dataProvider)
{
    var ret = {
        commandLine: [ "/usr/bin/python",
                        "/fastqc_app.py",
                        "/data/input",
                        "/data/output",
                        "/data/scratch",
                        "/data/logs"
                    ],
        containerImageId: "DOCKER_IMAGE[:TAG]",
        Options: [ "bsfs.enabled=true" ]
    };
    return ret;
}