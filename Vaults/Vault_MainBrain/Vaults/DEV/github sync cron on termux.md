# Guide: Obsidian vault github sync cron on termux

A [guide](https://www.reddit.com/r/ObsidianMD/comments/qep4gn/guide_obsidian_vault_github_sync_cron_on_termux/) on how to sync an obsidian vault over github using git, bash script and cron (cronie).

## Reference:

1. [Main bash script and cron's crontab source](https://forum.obsidian.md/t/obsidian-github-integration-for-sync-and-version-control/6369)
    
2. [Secondary crond automation in termux](https://www.reddit.com/r/termux/comments/i27szk/how_do_i_crontab_on_termux/g02pghj?utm_medium=android_app&utm_source=share&context=3)
    

## Pre-requisites:

1. Functioning vault's git directory with push/pull to github repo (Look up ref 1 on how to create one).
    
2. [Cronie](https://github.com/cronie-crond/cronie), can install by `pkg install cronie` (required to schedule a bash script).
    
3. [Termux-services](https://wiki.termux.com/wiki/Termux-services), can install by `pkg install termux-services` (required for autolaoding of `crond`).

# Other Links
- [Obsidian with GitHub: A Guide to Organizing Your Digital Brain](https://medium.com/@yanfernandes404/unleash-the-power-of-obsidian-with-github-a-guide-to-organizing-your-digital-brain-4e516a2a62c)
- [Using Obsidian with Termux and VIM](https://www.thegadhian.com/posts/using-obsidian-with-termux-and-vim/)
- 
