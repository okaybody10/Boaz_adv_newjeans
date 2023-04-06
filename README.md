# Boaz_adv_Newjeans
Root repository for the Boaz ADV Session

# Subject & Keywords
* Subject: Fake news detection through article text and photos
* Keywords: Multimodal, Fake news, classification

# Brief introduction
* Our project is inspired by this [paper](https://github.com/faiazrahman/Multimodal-Fake-News-Detection)
  * We will change the above model as we have more than one photo.
    * Not determined yet
    * The simplest idea: concat photos and pass through resnet152, and finally 1-D convolution to reduce size (we can finally add attention layer, and finally pass FC).
    * Second idea: First summarizing the text and retrieving (or finding the attention weight) per paragraph, and normalizing the photographs (or selecting only one photograph).
  * Here is the papers we referenced in addition to that above
    * [paper](https://scienceon.kisti.re.kr/commons/util/originalView.do?cn=CFKO201826259815374&oCn=NPAP12689273&dbt=CFKO&journal=NPRO00377585)
* Since we are going to use the Korean dataset, we have crawled the articles based on the data provided by [this site](https://factcheck.snu.ac.kr/) about the fake news and the real news.

# TODO list
[] Modify the code and dataset
 - Find the korean sentence model (e.g. snunlp, sentence-klue-roberta-base)
 - Run the sample code and get the embedding size, and modify them (if necessary)
[] Run code on GPU
 - Colab? Laboratory?
