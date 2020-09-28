
while :
do
    echo "Running @ $(date)"
    # grab new images and analyze
    python3 analyze-image.py
    python3 detection.py

    # push to the DB
    python3 datastore.py
    
    # push to the DB 
    # wait for next round
    sleep 300 # every 5-minutes 
done
