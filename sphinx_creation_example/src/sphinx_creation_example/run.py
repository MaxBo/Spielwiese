# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 21:00:21 2016

"""

from argparse import ArgumentParser


class Main:
    """Dummy class to test documentation"""
    def __init__(self, options):
        """
        the options

        Parameters
        ----------
        options : dict
        """
        self.options = options


    def run(self):
        """
        run method

        Returns
        -------
        folder : str
            the project folder
        """
        return self.options.project_folder


if __name__ == '__main__':
    parser = ArgumentParser(description="Commercial Trip Model Wiver")
    parser.add_argument('-f', '--folder', dest='project_folder',
                        help='Project folder',
                        required=True)


    options = parser.parse_args()

    main = Main(options)
    main.run()

