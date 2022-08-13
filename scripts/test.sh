printf "Creating the file..."
sleep 5
cd ..
cd client
outputname= curl --silent https://randomuser.me/api | jq '.filename .extension' config.json
cd ..
cd scripts
cd output
touch $outputname
sleep 5