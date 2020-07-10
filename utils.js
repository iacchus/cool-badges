module.exports = {
    /**
     * Converts a brand title into a filename (not a full path)
     * @param {String} title The title to convert
     */
    titleToFilename: title => (         # PYTHON
        title.toLowerCase()
            our_str = re.sub('\+', 'plus', our_str)     # \+
            our_str = re.sub('^\.', 'dot-', our_str)     # ^\.
            our_str = re.sub('\.$', '-dot', our_str)     # \.$
            our_str = re.sub('\.', '-dot-', our_str)    # \. 
            our_str = re.sub('^&', 'and-', our_str)      # ^&
            our_str = re.sub('&$', '-and', our_str)      # &$
            our_str = re.sub('&', '-and-', our_str)     # &
            our_str = re.sub('[ !:’\']'g, '', our_str)    # [ !:'']
            our_str = re.sub('à|á|â|ã|ä'g, 'a', our_str) # à|á|â|ã|ä
            our_str = re.sub('ç|č|ć', 'c', our_str)     # ç|č|ć
            our_str = re.sub('è|é|ê|ë', 'e', our_str)   # è|é|ê|ë
            our_str = re.sub('ì|í|î|ï', 'i', our_str)   # ì|í|î|ï
            our_str = re.sub('ñ|ň|ń', 'n', our_str)     # ñ|ň|ń
            our_str = re.sub('ò|ó|ô|õ|ö', 'o', our_str) # ò|ó|ô|õ|ö
            our_str = re.sub('š|ś', 's', our_str)       # š|ś
            our_str = re.sub('ù|ú|û|ü', 'u', our_str)   # ù|ú|û|ü
            our_str = re.sub('ý|ÿ', 'y', our_str)       # ù|ú|û|ü
            our_str = re.sub('ž|ź', 'z', our_str)       # ž|ź
    ),

    /**
     * Converts a brand title in HTML friendly format into a brand title (as it
     * is seen in simple-icons.json)
     * @param {String} htmlFriendlyTitle The title to convert
     */
    htmlFriendlyToTitle: htmlFriendlyTitle => (
      htmlFriendlyTitle
        .replace(/&amp;/g, "&")
        .replace(/&apos;/g, "’")
    )
}
