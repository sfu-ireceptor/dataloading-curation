# Get the absolute path of the current makefile
MAKEFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
# Create a temporary directory that we can work in.
TMP_DIR := $(shell mktemp -d)

all:	airr repertoires rearrangements clones
repertoires:	ir-repertoire airr-repertoire mhc-genotype
airr:	airr-rearrangement airr-clone airr-cell airr-link airr-reactivity
rearrangements:	imgt mixcr igblast adaptive
clones:	mixcr-clone

ir-repertoire:
	./scripts/load_metadata.sh ireceptor $(MAKEFILE_DIR)/$@/metadata_10.csv
airr-repertoire:
	./scripts/load_metadata.sh repertoire $(MAKEFILE_DIR)/$@/florian.airr.json
mhc-genotype:
	./scripts/load_metadata.sh ireceptor $(MAKEFILE_DIR)/$@/Culina-CerosalettiLab0145-metadata.csv
	echo "subject_id\trepertoire_id\tdata_processing_id\tsample_processing_id\tdata_processing_files" > ${TMP_DIR}/repertoires.tsv
	curl -s -k -d '{"filters":{"op":"=","content":{"field":"subject.subject_id","value":"CerosalettiLab0145"}},"fields":["subject.subject_id","repertoire_id","sample.sample_processing_id","data_processing.data_processing_id","data_processing.data_processing_files"]}' https://localhost/airr/v1/repertoire | jq --raw-output '.Repertoire[] | [.subject.subject_id, .repertoire_id, .data_processing[].data_processing_id, .sample[].sample_processing_id, .data_processing[].data_processing_files | if type == "array" then join(", ") else . end] | @tsv' >> ${TMP_DIR}/repertoires.tsv
	mkdir ${TMP_DIR}/mhc
	python3 ${SANDBOX_DIR}/mhc2airr/mhc2airr-json.py $(MAKEFILE_DIR)/$@/Culina-CerosalettiLab0145-mhc.tsv ${TMP_DIR}/repertoires.tsv ${TMP_DIR}/mhc
	./scripts/update_metadata.sh repertoire ${TMP_DIR}/mhc/*.json
	rm ${TMP_DIR}/mhc/*.json
	rmdir ${TMP_DIR}/mhc
	rm ${TMP_DIR}/repertoires.tsv

airr-rearrangement:
	./scripts/load_metadata.sh ireceptor $(MAKEFILE_DIR)/$@/*.csv
	./scripts/load_rearrangements_no_index_build.sh airr $(MAKEFILE_DIR)/$@/*.tsv
airr-clone:
	./scripts/load_metadata.sh ireceptor $(MAKEFILE_DIR)/$@/*.csv
	./scripts/load_clones.sh airr-clone $(MAKEFILE_DIR)/$@/*.json
airr-cell:
	./scripts/load_metadata.sh ireceptor $(MAKEFILE_DIR)/$@/*.csv
	./scripts/load_cells.sh airr-cell $(MAKEFILE_DIR)/$@/*-cells.json
	./scripts/load_expression.sh airr-expression $(MAKEFILE_DIR)/$@/*-gex.json
airr-reactivity:
	./scripts/load_metadata.sh ireceptor $(MAKEFILE_DIR)/$@/PRJNA744851-Minervina/R23-cell-reactivity-metadata.csv
	./scripts/load_cells.sh airr-cell $(MAKEFILE_DIR)/$@/PRJNA744851-Minervina/R23_inf_vax2-t-cells.json
	./scripts/load_reactivity.sh airr-reactivity $(MAKEFILE_DIR)/$@/PRJNA744851-Minervina/R23_reactivity.json
	./scripts/link_reactivity2cell.sh $(MAKEFILE_DIR)/$@/PRJNA744851-Minervina/R23-reactivity-to-cell.tsv

airr-link:
	./scripts/link_expression2cell.sh $(MAKEFILE_DIR)/$@/expression2cell.tsv
	./scripts/link_rearrangement2clone.sh $(MAKEFILE_DIR)/$@/clone2rearrangement.tsv
	./scripts/link_rearrangement2cell.sh $(MAKEFILE_DIR)/$@/rearrangement2cell.tsv

igblast:
	./scripts/load_metadata.sh ireceptor $(MAKEFILE_DIR)/$@/analy13_sample.csv
	./scripts/load_rearrangements_no_index_build.sh airr $(MAKEFILE_DIR)/$@/analy13.igblast_airr_annots.tsv
imgt:
	./scripts/load_metadata.sh ireceptor $(MAKEFILE_DIR)/$@/PRJNA248411_Palanichamy_2018-12-18.csv
	./scripts/load_rearrangements_no_index_build.sh imgt $(MAKEFILE_DIR)/$@/SRR*.txz
mixcr:
	./scripts/load_metadata.sh ireceptor $(MAKEFILE_DIR)/$@/PRJNA330606_Wang_One_Sample.csv
mixcr-clone:
	./scripts/load_metadata.sh ireceptor $(MAKEFILE_DIR)/$@/IR-Binder-000001_metadata_2020-07-21.csv
	./scripts/load_clones.sh mixcr-clone $(MAKEFILE_DIR)/$@/TRB-Pt-1-8_S150.clones.txt
adaptive:
	./scripts/load_metadata.sh ireceptor $(MAKEFILE_DIR)/$@/860011108_TCRB_metadata.csv
	./scripts/load_rearrangements_no_index_build.sh adaptive $(MAKEFILE_DIR)/$@/860011108_TCRB-500.tsv
