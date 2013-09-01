#!/usr/bin/env python
# coding=utf-8
'''
This script will help you take out all strings.xml(Placed in a language-region folder) from an Android projectDir
We now use it to provide the strings and upload them to Crowdin.



'''
from os import system,listdir,path
from sys import argv

def takeoutStrings(resPath):
    for item in listdir(resPath):
        itemPath = resPath + '/' + item
        print item
        if (not 'values' in item) :
            rmUnused = 'rm -rf %s'%(itemPath)
            print rmUnused
            system(rmUnused)
            continue

        if ('large' in item or 'dpi' in item):
            rmLayout = 'rm -rf %s'%(itemPath)
            print rmLayout
            system(rmLayout)
            continue


        if (not path.isdir(itemPath)):
            rmFile = 'rm -rf %s'%(itemPath)
            print rmFile
            system(rmFile)
            continue

        for subItem in listdir(itemPath):
            subItemPath = itemPath + '/' + subItem
            if (not 'strings.xml' == subItem):
                rmNotStrings = 'rm -rf %s'%(subItemPath)
                print rmNotStrings
                system(rmNotStrings)
        
        if (len(listdir(itemPath)) == 0):
            removeEmptyFolder = 'rm -rf %s'%(itemPath)
            print 'Removing empty folder %s'%(itemPath)
            system(removeEmptyFolder)


def main():
    '''
    Usage: takeoutStrings.py projectPath
    '''
    if (len(argv) < 2) :
        print main.__doc__
        return
    projectDir = argv[1]
    projResDir = projectDir + '/res/'
    destBaseDir = '/tmp/'
    destDir = '/tmp/res/'
    cpRes = 'cp %s %s -rf '%(projResDir, destBaseDir)
    print cpRes
    system(cpRes)
    takeoutStrings(destDir)

main()

        


