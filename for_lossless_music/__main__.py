#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import for_lossless_music as flm


def main(**kwargs):
    parser = argparse.ArgumentParser(
        prog='for-lossless-music',
        usage='for-lossless-music [OPTION]... Keyword | QQ music encryption directory',
        description='For lossless music!',
    )

    parser.add_argument(
        '-V', '--version', action='store_true',
        help='Print version'
    )

    search_grp = parser.add_argument_group('Search options')
    search_grp.add_argument(
        '-s', '--source', metavar='source', default=flm.Source.QQ,
        help='Which source you want to search. now support: qq(QQ), kw(酷我), default source is qq'
    )

    search_grp.add_argument(
        '-p', '--page', metavar='page', type=int, default=1,
        help='What page do you what to display, default is 1'
    )

    search_grp.add_argument(
        '-n', '--num', metavar='num', type=int, default=20,
        help='How many rows are display on a page'
    )

    download_grp = parser.add_argument_group('Download options')

    download_grp.add_argument(
        '-i', '--index', metavar='SONG ID', type=int, default=-1,
        help='song index, e.g. -i 1'
    )

    download_grp.add_argument(
        '-o', '--output', metavar='OUTPUT PATH', default='.',
        help='output path'
    )

    download_grp.add_argument(
        '-c', '--classify', action='store_true',
        help='Classify by singer'
    )

    parser.add_argument('keyword', nargs='+', help=argparse.SUPPRESS)

    args = parser.parse_args()

    if args.version:
        print(flm.__version__)

    if len(args.keyword) > 1:
        print("Too many keywords")
        sys.exit()

    source = flm.str2source(args.source)
    if not source:
        print('Could not find source ' + args.source)
        sys.exit()

    keyword = args.keyword[0]
    # if os.path.exists, keyword be identified as path
    # otherwise, keyword be identified as keyword
    if os.path.exists(keyword):
        input_path = os.path.abspath(keyword)
        found_songs = []

        def set_and_output_status(status):
            found_song.status = status
            found_songs.append(found_song)
            print(flm.foundsong2table([found_song], len(found_songs)))

        for e in os.listdir(input_path):
            try:
                fullpath = '{}/{}'.format(input_path, e)
                if not os.path.isfile(fullpath):
                    continue
                singer, songname = e[:e.rfind('.')].split('-')
                found_song = flm.FoundSong(songname, singer)
                total, songs = flm.Moresound.search(songname, source)
                for song in songs:
                    if song.name == songname and '/'.join(song.singers) == singer:
                        found_song.song = song
                        break

                if not found_song.song:
                    set_and_output_status('NOT FOUND')
                    continue

                # start download
                urls = flm.Moresound.get_download_urls(found_song.song)
                best_quality = flm.find_best_quality(urls)
                if not best_quality:
                    set_and_output_status('NOT FOUND')
                    continue

                output_path = os.path.abspath(args.output)
                if args.classify:
                    output_path += '/' + found_song.origin_singer
                os.makedirs(output_path, exist_ok=True)
                output_path = '{path}/{singer}-{songname}.{suffix}' \
                    .format(path=output_path,
                            singer=found_song.origin_singer,
                            songname=found_song.origin_name,
                            suffix=best_quality.lower(),
                            )

                if os.path.isfile(output_path):
                    set_and_output_status('FOUND | Local file EXISTS, SKIP')
                    continue
                flm.download(urls[best_quality], output_path)

                set_and_output_status('FOUND | DOWNLOAD SUCCESS')
                # end download
            except Exception as ex:
                set_and_output_status('ERROR ' + str(ex.args))
        print()
        print(flm.foundsong2table(found_songs))

    # if args.index not be input, this mean that mode is search
    elif args.index is -1:
        total, songs = flm.Moresound.search(keyword, source, args.page, args.num)
        table = flm.songs2table(songs)
        print('total', total)
        print(table)
    # args.index be set, mean mode is download
    else:
        total, songs = flm.Moresound.search(keyword, source, args.index, 1)
        if not len(songs):
            print('Could not find')
            sys.exit()
        print(flm.songs2table(songs))
        urls = flm.Moresound.get_download_urls(songs[0])
        best_quality = flm.find_best_quality(urls)
        if not best_quality:
            print('Could not find')
            sys.exit()
        singer = '/'.join(songs[0].singers)
        input_path = os.path.abspath(args.output)
        if args.classify:
            input_path += '/' + singer
        os.makedirs(input_path, exist_ok=True)
        flm.download(urls[best_quality],
                     '{path}/{singer}-{songname}.{suffix}'
                     .format(path=input_path,
                             singer=singer,
                             songname=songs[0].name,
                             suffix=best_quality.lower(),
                             )
                     )
