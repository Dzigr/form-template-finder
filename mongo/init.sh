#!/bin/bash

collections=("templates")

for collection in "${collections[@]}"
do
    echo "Importing $collection..."
    mongoimport --host $db_host --db $db_name --collection "$collection" --file "seed/$collection.json" --jsonArray --mode upsert -u root -p example --authenticationDatabase=admin

    if [ $? -eq 0 ]; then
        echo "Successfully imported $collection"
    else
        echo "Failed to import $collection"
    fi
done
