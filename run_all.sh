echo Analysis module starting...

./files.sh

if [ $? -eq 0 ]
then
    echo Data files found. Going to next step...
else
    echo Error: No data files exist!
fi

python3 file_names.py > newfiles.dat

echo Extracting data from files. Going to next step...

python3 extract_rdata.py > rdata.dat
if [ $? -eq 0 ]
then
   echo Extraction of data from files successful. Going to next step...
else
    echo Error: Problem in extracting data!
fi

python3 plot_numerical.py
if [ $? -eq 0 ]
then
   echo Process completed. Image saved successfully.
   echo Leaving Analysis module!
else
    echo Error: Can\'t generate image!
fi
