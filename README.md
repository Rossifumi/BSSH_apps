# BaseSpace custom apps

A summary of custom apps developed for BaseSpace

## UMItools

UMItools, third-party UMI tools, [CGATOxford](https://github.com/CGATOxford/UMI-tools)

### Short description

Version 1.0.0

UMItools v1.0.0 accepts fastq as input and generate dedup bam.

Version 2.0.0

v2.0.0 support reading bam from following apps: Enrichment, BWA Aligner, Whole Genome Sequencing, TruSight Tumor 170

Accept both pair-end and single-end BAM. Enable customer to set UMI separator.

### App deployment

* [BaseSpace US](https://basespace.illumina.com/apps/4437433/UMI_tools) - Version 1.0.0
* [BaseSpace US](https://basespace.illumina.com/apps/4992988/UMI_tools) - Version 2.0.0
* [BaseSpace China](https://cnn1.sh.basespace.illumina.com.cn/apps/82082/UMItools) - Version 1.0.0
* [BaseSpace China](https://cnn1.sh.basespace.illumina.com.cn/apps/83083/UMItools) - Version 2.0.0
* [BaseSpace Australia](https://aps2.sh.basespace.illumina.com/apps/25026/UMItools) - Version 1.0.0
* [BaseSpace Australia](https://aps2.sh.basespace.illumina.com/apps/25027/UMItools) - Version 2.0.0

## Trimmomatic_app

Trimmomatic, third-party preprocessing tools, [USADEL lab](http://www.usadellab.org/cms/?page=trimmomatic)

### App deployment

* [BaseSpace US](https://basespace.illumina.com/apps/4883879/Trimmomatic) 
* [BaseSpace China](https://cnn1.sh.basespace.illumina.com.cn/apps/9009/Trimmomatic) 

## Somatic_app

Somatic Variant Calling Pipeline, Illumina variant calling pipeline

### Short description

Somatic Variant Calling Pipeline calls small variants from FFPE samples.

Tools used are : [Hygea, Stitcher, Pisces](https://github.com/Illumina/Pisces) 

For UMI Error Correction app users, input should be BAM from CollapsedReads folder.

For non-UMI users, input should be BAM after mark duplication and sorting.

BAM output from BWA Aligner app and Enrichment app could be used as input for this app.

Output are by default gVCF file.

### App deployment

* [BaseSpace US](https://basespace.illumina.com/apps/5707703/Somatic-Variant-Calling-Pipeline) - Version 1.0.0
* [BaseSpace China](https://cnn1.sh.basespace.illumina.com.cn/apps/81081/Somatic-Variant-Calling-Pipeline) - Version 1.0.0
* [BaseSpace Australia](https://aps2.sh.basespace.illumina.com/apps/25025/Somatic-Variant-Calling-Pipeline) - Version 1.0.0

## Pisces527

Pisces Standalone, Illumina variant calling standalone tool, [Pisces Suite](https://github.com/Illumina/Pisces)

### App deployment

* [BaseSpace US](https://basespace.illumina.com/apps/5694689/Pisces-Standalone) - Version 1.0.0
* [BaseSpace China](https://cnn1.sh.basespace.illumina.com.cn/apps/80080/Pisces-Standalone) - Version 1.0.0

## DNA Amplicon with genomes

A fork version of DNA Amplicon that enables usage of common reference genomes.

### App deployment

* [BaseSpace US](https://basespace.illumina.com/apps/6148142/DNA-Amplicon-with-genome) - Version 1.1.1


## Other notes

### FastQC_demo_app

Developed for developer conferece, good materials to train new hires


## Acknowledgments

* Apps were developed based on this [python framework](https://git.illumina.com/pcherng/bssh-native-app-python) developed by Paul Cherng. 

