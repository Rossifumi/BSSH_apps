function launchSpec(dataProvider)
{
    var ret = {
        commandLine: [ "/usr/bin/python",
                        "/dna-amplicon-output-parser.py",
                        "/data/input",
                        "/data/output",
                        "/data/scratch",
                        "/data/logs"
                    ],
        containerImageId: "docker.illumina.com/jjxu/dna-amplicon-parser",
        Options: [ "bsfs.enabled=true" ]
    };
    return ret;
}