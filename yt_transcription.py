import argparse
from pytubefix import YouTube
from pathlib import Path


class yt_transcript:

    def __init__(self, yt_url):
        self.yt_url = yt_url
        self.get_captions()
        self.format_srt()
    
    def pull_and_write(self, output_file):
        self.get_captions()
        self.format_srt()
        self.write_transcript(output_file=output_file)

    def get_captions(self):
        yt = YouTube(self.yt_url)
        if "en" in yt.captions.keys():
            caption = yt.captions["en"]
        elif "a.en" in yt.captions.keys():
            caption = yt.captions["a.en"]
        else:
            print("no english language captions") # TODO: support other languages

        #caption = yt.captions.get_by_language_code('en')
        #caption.save_captions("captions.txt")
        self.srt = caption.generate_srt_captions()

    def format_srt(self):
        """

        Kind of a weird function
        The srt object we have, when split by newline into a list, looks like:
            [line number,
            timestamp,
            words in line,
            " ",
            ...]
        and it repeats, until the last line where the final " " is excluded.
        So we want split our string by newline, and then take that list and parse it
        so that we take sets of 4 elements of the list, collect the third element in
        that list, and append it to another list. The edge case is that the last set
        only has 3 elements, but we can write it so it doesn't mind 
        (mylist[0:4] doesn't complain if there's only 3 elements)
        """
        # split into lines
        # format is:
            # line number
            # timestamp
            # words in line
            # " "
        
            
        srt_list = self.srt.split('\n')
        num_chunks = len(srt_list)//4 + 1
        lines = []
        for i in range(0, num_chunks):
            lines.append(srt_list[i*4:i*4+4][2])
        self.formatted_captions = '\n'.join(lines)

    def write_transcript(self, output_file):
        with open(output_file, 'w') as f:
            f.write(self.formatted_captions)


