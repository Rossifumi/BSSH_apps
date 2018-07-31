function isLetterOrDigit(e) { var t = /^[0-9a-zA-Z]+$/; return e.match(t) ? !0 : !1 } function getStrictFilenameFriendlyName(e) { if (null === e) return null; for (var t = "", a = 0; a < e.length; a++) t += e.charCodeAt(a) > 127 || !isLetterOrDigit(e[a]) && "_" !== e[a] ? "-" : e[a]; return t } function trimFileExtension(e) { return e.replace(/\.[^\/.]+$/, "") } var MapPair = function () { function e(e) { for (var t = [], a = 1; a < arguments.length; a++) t[a - 1] = arguments[a]; this.Key = e, this.Values = t } return e }(), BsMap = function () { function e() { this.ItemsMap = [] } return e }(), SampleSheet = function () { function e() { this.header = [new MapPair("SampleSheetSection", "Header")], this.settings = [new MapPair("SampleSheetSection", "Settings")], this.manifests = [new MapPair("SampleSheetSection", "Manifests")], this.data = [] } return e.prototype.addHeader = function (e, t) { this.header.push({ Key: e, Values: [t] }) }, e.prototype.addSetting = function (e, t) { this.settings.push({ Key: e, Values: [t] }) }, e.prototype.addManifest = function (e) { for (var t = [], a = 1; a < arguments.length; a++) t[a - 1] = arguments[a]; for (var s = 0; s < t.length; s++) for (var i = t[s], r = 0; r < i.samples.length; r++) { var n = i.samples[r]; this.manifests.push({ Key: n.Id + "-" + i.propertyName, Values: [e] }) } }, e.prototype.addGlobalManifest = function (e) { this.manifests.push({ Key: "Global", Values: [e] }) }, e.prototype.addRawData = function (e, t) { for (var a = [], s = 2; s < arguments.length; s++) a[s - 2] = arguments[s]; var i = [new MapPair("SampleSheetSection", "RawDataEntry"), new MapPair("Sample_ID", e), new MapPair("Sample_Name", t)].concat(a); this.data.push(i) }, e.prototype.addData = function (e) { for (var t = [], a = 1; a < arguments.length; a++) t[a - 1] = arguments[a]; for (var s = [new MapPair("SampleSheetSection", "Data"), new MapPair("BaseSpacePropertyName", e.propertyName)].concat(t), i = 0; i < e.samples.length; i++) { var r = e.samples[i]; s.push(new MapPair("SampleResourceId", r.Id)) } this.data.push(s) }, e.prototype.addGlobalData = function () { for (var e = [], t = 0; t < arguments.length; t++) e[t - 0] = arguments[t]; var a = [new MapPair("SampleSheetSection", "Data"), new MapPair("SampleResourceId", "Global")].concat(e); this.data.push(a) }, e.prototype.getMap = function () { var e = new BsMap; return this.header.length > 1 && e.ItemsMap.push(this.header), this.settings.length > 1 && e.ItemsMap.push(this.settings), this.manifests.length > 1 && e.ItemsMap.push(this.manifests), e.ItemsMap = e.ItemsMap.concat(this.data), e }, e }(), AppResultConfiguration = function () { function e() { this.appResultGroups = [] } return e.prototype.addAppResult = function (e) { var t = this.getUniqueAppResultName(e.name), a = [{ Key: "Name", Values: [t] }]; "description" in e ? a.push({ Key: "Description", Values: [e.description] }) : a.push({ Key: "Description", Values: [e.name] }); for (var s = [], i = 0; i < e.sampleProperties.length; i++) for (var r = e.sampleProperties[i], n = 0; n < r.samples.length; n++) { var p = r.samples[n]; s.push(r.propertyName + ":" + p.Id) } if (a.push({ Key: "SampleProperties", Values: s }), "properties" in e) for (var n = 0; n < e.properties.length; n++) { var u = e.properties[n], o = "description" in u ? u.description : u.name, l = "Property-" + u.name; a.push({ Key: l, Values: [o].concat(u.values) }) } if ("fileSuffixes" in e && a.push({ Key: "FileSuffixes", Values: e.fileSuffixes }), "exactFileNames" in e && a.push({ Key: "ExactFileNames", Values: e.exactFileNames }), "directories" in e && a.push({ Key: "Directories", Values: e.directories }), "zipFiles" in e) for (var h = 0; h < e.zipFiles.length; h++) { var f = e.zipFiles[h], m = [f.name]; if ("fileSuffixes" in f) for (var c = 0; c < f.fileSuffixes.length; c++) m.push("FileSuffixes=>" + f.fileSuffixes[c]); if ("exactFileNames" in f) for (var g = 0; g < f.exactFileNames.length; g++) m.push("ExactFileNames=>" + f.exactFileNames[g]); a.push({ Key: "Zip-" + (h + 1), Values: m }) } return this.appResultGroups.push(a), t }, e.prototype.getUniqueAppResultName = function (t) { for (var a = t, s = 0; a in e.appResultNames;) a = t + " (" + ++s + ")"; return e.appResultNames[a] = !0, a }, e.prototype.getMap = function () { var e = new BsMap; return e.ItemsMap = this.appResultGroups, e }, e.appResultNames = new Object, e }();/// <reference path="../../Illumina.BaseSpace.NativeApp.Isas/Illumina.BaseSpace.NativeApp.Isis/Illumina.BaseSpace.NativeApp.Isis/callbacks.js/isis.callbacks.lib.ts"/>
// Note that, if GenomeResourceUrl is set in the sample sheet, only the keys are used and the paths/values are ignored.
var genomesMap = [[
    { "Key": "hg19", "Values": ["/genomes/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFasta"] },
    { "Key": "GRCh38Decoy", "Values": ["/genomes/Homo_sapiens/NCBI/GRCh38Decoy/Sequence/WholeGenomeFasta"] },
    { "Key": "mm9", "Values": ["/genomes/Mus_musculus/UCSC/mm9/Sequence/WholeGenomeFasta"] },
    { "Key": "rn4", "Values": ["/genomes/Rattus_norvegicus/UCSC/rn4/Sequence/WholeGenomeFasta"] },
    { "Key": "UMD3.1", "Values": ["/genomes/Bos_taurus/Ensembl/UMD3.1/Sequence/WholeGenomeFasta"] },
    { "Key": "AGPv3", "Values": ["/genomes/Zea_mays/Ensembl/AGPv3/Sequence/WholeGenomeFasta"] },
    { "Key": "IRGSP-1.0", "Values": ["/genomes/Oryza_sativa_japonica/Ensembl/IRGSP-1.0/Sequence/WholeGenomeFasta"] },
    { "Key": "Sscrofa10.2", "Values": ["/genomes/Sus_scrofa/Ensembl/Sscrofa10.2/Sequence/WholeGenomeFasta"] },
    { "Key": "CanFam3.1", "Values": ["/genomes/Canis_familiaris/Ensembl/CanFam3.1/Sequence/WholeGenomeFasta"] },
    { "Key": "Gm01", "Values": ["/genomes/Glycine_max/Ensembl/Gm01/Sequence/WholeGenomeFasta"] },
    { "Key": "Galgal4", "Values": ["/genomes/Glycine_max/Ensembl/Galgal4/Sequence/WholeGenomeFasta"] },
    { "Key": "Oar_v3.1", "Values": ["/genomes/Ovis_aries/Ensembl/Oar_v3.1/Sequence/WholeGenomeFasta"] },
]];
var manifestMap = {
    "AmpliSeq for Illumina Cancer HotSpot Panel v2 (20171207)": "/opt/App/Plugin/FixedManifests/CancerHotSpot-v2.dna_manifest.20171207.txt",
    "AmpliSeq for Illumina Comprehensive Cancer Panel (20171207)": "/opt/App/Plugin/FixedManifests/ComprehensiveCancer.dna_manifest.20171207.txt",
    "AmpliSeq for Illumina Exome Panel (20171207)": "/opt/App/Plugin/FixedManifests/Exome.dna_manifest.20171207.txt",
    "TruSeq Amplicon - Cancer Panel (AFP1)": "/opt/App/Plugin/FixedManifests/truseq_amplicon_cancer_panel_manifest_afp1_pn15032433_b.txt",
    "TruSight Cancer Hotspot Panel": "/opt/App/Plugin/FixedManifests/truseq_amplicon_cancer_panel_manifest_afp1_pn15032433_b.txt",
    "TruSight Myeloid Sequencing Panel": "/opt/App/Plugin/FixedManifests/TruSightMyeloid_manifest.txt",
    "TruSeq Custom Amplicon Control Pool 1 (ACP1)": "/opt/App/Plugin/FixedManifests/truseq_custom_amplicon_control_manifest_acp1.txt",
    "TruSeq Custom Amplicon Control Pool 3 (ACP3)": "/opt/App/Plugin/FixedManifests/truseq_amplicon_cancer_panel_manifest_afp1_pn15032433_b.txt"
};
var nirvanaGenomes = ["hg19", "GRCh38Decoy"];

/*
function FormUpdates(dataProvider){
    var wholeGenomeFasta = dataProvider.GetProperty("Input.whole-genome-fasta");
    
    // custom genome
    if (wholeGenomeFasta){
        dataProvider.AttributeUpdates.Add({ ElementId: "annotation-source", AttributeName: "disabled", AttributeValue: "disabled" });
    }else{
        dataProvider.AttributeUpdates.Remove({ ElementId: "annotation-source", AttributeName: "disabled" });
    }
}
*/

function launchSpec(dataProvider) {
    var appSessionName = dataProvider.GetProperty("Input.app-session-name");
    var appName = "DNA Amplicon";
    var appVersion = "1.1.0";
    var samples = dataProvider.GetProperty('Input.sample-id');
    var appResults = dataProvider.GetProperty("Input.AppResults");
    var files = dataProvider.GetProperty("Input.Files");
    var outputProject = dataProvider.GetProperty("Input.project-id");
    
    //Genomes
    //var fixedGenome = dataProvider.GetProperty("Input.genomes-map");
    
    var wholeGenomeFasta = dataProvider.GetProperty("Input.whole-genome-fasta");
    var fixedManifest = dataProvider.GetProperty("Input.manifest-id");
    var customManifest = dataProvider.GetProperty("Input.custom-manifest");
    var aligner = dataProvider.GetProperty("Input.aligner");
    var variantCaller = dataProvider.GetProperty("Input.variant-caller");
    var somaticVariantCallerThreshold = dataProvider.GetProperty("Input.somatic-variant-caller-threshold") / 100;
    var variantCallerDepthFilter = dataProvider.GetProperty("Input.variant-caller-depth-filter");
    var forcedGenotypingVcfs = dataProvider.GetProperty("Input.forced-genotyping-vcfs");
    //var readStitching = dataProvider.GetProperty("Input.read-stitching");
    var readStitching = "1";
    var annotationSource = dataProvider.GetProperty("Input.annotation-source");
    var scylla = "1";
    if (forcedGenotypingVcfs) { scylla = "0"; }
    scylla = "0"; // Turn off Scylla for now. TODO: Remove when Scylla is fixed
    var hygea = dataProvider.GetProperty("Input.hygea");
    
    var imageTag = "@sha256:7a40012529555c141016660c277affb3fb55e7488942beb7c56d26da1b4b8e6b";
    var ret = { nodes: [] };
    var sampleSheet = new SampleSheet();
    sampleSheet.addHeader("Workflow", appName);
    sampleSheet.addSetting("AnalysisName", appSessionName);
    sampleSheet.addSetting("AppName", appName);
    sampleSheet.addSetting("AppVersion", appVersion);
    if (wholeGenomeFasta) {
        annotationSource = "none"; // turn off annotation if using a custom genome
    }
    sampleSheet.addSetting("ReadOnlyGenomeRepositoryFolder", "/tmp");
    sampleSheet.addSetting("GenomeResourceUrl", "s3://use1-prd-seq-hub-appdata/TruSeqAmplicon_v3/;s3://use1-prd-seq-hub-appdata/DNAAmplicon_v1/");
    sampleSheet.addSetting("AWSRegion", "us-east-1");
    sampleSheet.addSetting("GenomeArchiveName", "root.tar.gz");
    sampleSheet.addSetting("WritableGenomeRepositoryFolder", "/data/scratch/IsasGenomesLoaderResources");
    sampleSheet.addSetting("GenomeResourcePublicS3", "1");
    sampleSheet.addSetting("GenomeRepositoryLatestDateTime", "2018/01/01");
    if (aligner == "BWAWholeGenome") {
        sampleSheet.addSetting("Aligner", "BWA");
        sampleSheet.addSetting("RunBWAaln", "0");
        sampleSheet.addSetting("AmpliconReference", "WholeGenome");
    }else if (aligner == "BWATargeted") {
        sampleSheet.addSetting("Aligner", "BWA");
        sampleSheet.addSetting("RunBWAaln", "0");
        sampleSheet.addSetting("AmpliconReference", "Targeted");
    }else {
        sampleSheet.addSetting("Aligner", aligner);
        sampleSheet.addSetting("StitchReads", readStitching);
    }    
    sampleSheet.addSetting("VariantCaller", variantCaller);
    sampleSheet.addSetting("VariantCallerUseScylla", scylla); // Use Scylla to call MNVs?
    sampleSheet.addSetting("VariantCallPhasedSNP", scylla == "1" ? "0" : "1"); // Turn off MNV calling in Pisces if using Scylla
    sampleSheet.addSetting("VariantCallerRealignIndels", hygea); // Use Hygea to realign indels
    if (variantCaller === "PiscesSomatic") {
        sampleSheet.addSetting("variantfrequencyfiltercutoff", "" + somaticVariantCallerThreshold);
        sampleSheet.addSetting("MinimumCoverageDepth", variantCallerDepthFilter);
        sampleSheet.addSetting("VariantFilterRMxN", "3,6,0.20");
    }else {
        sampleSheet.addSetting("MinimumCoverageDepth", variantCallerDepthFilter);
        sampleSheet.addSetting("VariantFilterRMxN", "5,9,0.35");
    }
    if (annotationSource === "none") {
        sampleSheet.addSetting("VariantAnnotation", "None");
    }else {
        sampleSheet.addSetting("VariantAnnotation", "Nirvana");
        sampleSheet.addSetting("TranscriptSource", annotationSource);
        sampleSheet.addSetting("AnnotationDatabaseVersion", "84");
    }
    sampleSheet.addSetting("GenerateAggregates", "0");
    
    //Genomes
    //if (fixedGenome !== "custom") {
    //    var fixedGenomeFilePath = genomesMap[fixedGenome];
    //    sampleSheet.addSetting("GenomeFolder",);
    //}
    
    if (fixedManifest !== "custom") {
        var fixedManifestFilePath = manifestMap[fixedManifest];
        sampleSheet.addGlobalManifest(fixedManifestFilePath);
    }else {
        sampleSheet.addGlobalManifest(customManifest.Id);
    }
    var maxNodes = 99;
    var maxSamplesPerNode = Math.max(6, Math.ceil(samples.length / maxNodes));
    var count = 0;
    var appResultConfiguration = new AppResultConfiguration();
    var nodeSamples = [];
    for (var i = 0; i < samples.length; i++) {
        var sample = samples[i];
        nodeSamples.push(sample);
        var sampleNumber = count + 1;
        var safeName = getStrictFilenameFriendlyName(sample.Name);
        var sampleFilePrefix = safeName + "_S" + sampleNumber + ".";
        appResultConfiguration.addAppResult({
            name: sample.Name,
            sampleProperties: [{
                    propertyName: "Input.sample-id",
                    samples: [sample]
                }],
            fileSuffixes: [
                "bam",
                "bam.bai",
                "coverage.csv",
                "coverage.plot.csv",
                "baseCoverage.csv",
                "genotype.csv",
                "genotype.vcf",
                "genome.vcf.gz",
                "genome.vcf.gz.tbi",
                "report.html",
                "report.pdf",
                "summary.csv",
                "varianttable.txt",
                "vcf.gz",
                "vcf.gz.tbi",
                "annotations.json.gz",
                "dataset.json=>.basespace/dataset.json"
            ],
            exactFileNames: [
            ]
        });
        count++;
        if (count === maxSamplesPerNode || i === samples.length - 1) {
            ret.nodes.push({
                commandLine: ["mono",
                    "/opt/App/Illumina.BaseSpace.NativeApp.Host.exe",
                    "-p=/opt/App/Plugin",
                    "-c=IsisPath:/opt/illumina/Isas/latest/Isas",
                    "-c=apiUrl:$ApiUrl"],
                containerImageId: "docker.illumina.com/jjxu/dna-amplicon-genomes",
                //containerImageId: "docker.illumina.com/coreappsproduction/truseqamplicon-master@sha256:7a40012529555c141016660c277affb3fb55e7488942beb7c56d26da1b4b8e6b",
                HostBuild: "Fast",
                Options: ["bsfs.enabled=true", "genomes.enabled=true", "EnableAwsUploader"],
                properties: {
                    "Input.Samples": nodeSamples,
                    "Input.sample-id": nodeSamples,
                    "Output.Projects": [outputProject],
                    "Input.project-id": [outputProject],
                    "Input.AppResults": appResults,
                    "Input.Files": files,
                    "Isis.StartAfterStep": "0",
                    "Isis.MaxAttempts": "3",
                    "Isis.SampleSheetConfiguration": sampleSheet.getMap(),
                    "Isis.AppResultConfiguration": appResultConfiguration.getMap(),
                    "Input.genomes-map": genomesMap,
                    "Input.annotation-genomes": nirvanaGenomes,
                    "Input.whole-genome-fasta": wholeGenomeFasta,
                    "Input.forced-genotyping-vcfs": forcedGenotypingVcfs
                }
            });
            count = 0;
            appResultConfiguration = new AppResultConfiguration();
            nodeSamples = [];
        }
    }
    return ret;
}
