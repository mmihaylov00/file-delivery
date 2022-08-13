printf "Creating the file..."
sleep 5
cd ..
cd client
outputname = jq '.filename + .extension' config.json
cd ..
cd scripts
cd output
touch outputname