# ObjectFilesearch
Search File Systems and Object Repositories 
Show possibilities : 

Index Filename/Objects to search for Filenames and Index human readable content (PDF , WORD ..)
Future Ideas include Pictures and other content .


Example to Search Shares and Objectstores in Python , using Elasticsearch .
Including Docker Container Build and Nutanix Calm for automated Install & Setup

Create Elasticsearch Container 
docker build -t elasticsearch-plugin1 .
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.6.2

Run Kibana connect to Elasticsearch 
docker run --link 52158108abdf:elasticsearch -p 5601:5601 docker.elastic.co/kibana/kibana:7.6.2


