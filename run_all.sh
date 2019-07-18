echo 'Analysis module starting...'
./files.sh
echo 'Data files found!'
python3 file_names.py > newfiles.dat
echo 'Extracting data from files!'
python3 extract_rdata.py > rdata.dat
echo 'Extraction of data from files successful!'
python3 plot_numerical.py
echo 'Image saved successfully!'
