# Codeforces Submitter Plugin Vim

This plugin helps you in submitting your solutions to codeforces while practicing.

#Installation

To install this plugin just run the following commands on your terminal:

`cd ~/.vim/bundle`

`git clone https://github.com/JustAnAverageGuy/codeforces_submitter.vim.git`

## Configuration

Configure the script by providing it with your handle, password and default LanguageId.
To do so, hardcode the values in `lines 14, 15, 16` of [plugin/CF.vim](plugin/CF.vim#L14)

Find language code for your preferred language in [language_codes.md](language_codes.md)
Add your handle in [plugin/checker.py](plugin/checker.py)

## Dependencies

You need to have python with beautiful soup and requests library installed.

## Usage 

> [!IMPORTANT]
> the problem URL needs to be somewhere in the source code

Calling 

`:CodeForceSubmit`

submits the problem.

Note that depending on your network speed, it may take a few seconds to show you the confirmation. 

To see your last verdict use

`:LastVerdict`

## Notes

The code is adapted from `github.com/KannaNeko/dew`.
