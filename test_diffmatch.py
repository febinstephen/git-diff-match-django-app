from diff_match_patch import diff_match_patch
dmp = diff_match_patch()
diffs = dmp.diff_main('Good dog', 'Bad dog')
print diffs
print dmp.diff_cleanupSemantic(diffs)
print dmp.diff_prettyHtml(diffs)
