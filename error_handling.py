#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import requests

TEMPORARY_ERROR_CODES  = (408,500,502,503,504)


def main():
  """
  メインの処理
  """
  response = fetch('http://httpbin.org/status/200,404,503')
  if 200 <= response.status_code <300:
    print('Success!')
  else:
    print('error!')


def fetch(url):
  """
  指定したurlを取得してResponseオブジェクトを変えす。一次的なエラーが起きた場合は最大三回リトライする。
  """
  max_retries = 3#最大リトライ回数
  retries = 0 #現在のリトライ数
  while True:
    try:
      print('Retrieving{0}...'.format(url))
      response=requests.get(url)
      print('Status:{0}'.format(response.status_code))
      if response.status_code not in TEMPORARY_ERROR_CODES:
        return response
    except requests.exceptions.RequestException as ex:
        #ネットワークレベルのエラーの場合はリトライする。
        print('Exception occured:{0}'.format(ex))
        retries += 1
        if retiries >= max_retries:
          raise Exception('Toomany retries.')

          wait = 2**(retries-1)
          print('Waiting {0} seconds...'.format(wait))
          time.sleep(wait)



if __name__ =="__main__":
  main()
