# 9. Using GitHub

[Git basics](08-git-basics.md) showed you how to save snapshots on your own
machine. **GitHub** is a website that stores a copy of your repository online. It
gives you three things: a **backup**, a way to **share** your work, and a place
to **collaborate** with others.

Git and GitHub are not the same thing: git is the tool, GitHub is one place to
keep git repositories. (GitLab and Azure DevOps are alternatives that work the
same way.)

## The one safety rule, first

Putting code on GitHub can make it visible to the world. **Before you push,
be sure there's no data and no secrets in your repository.** This template's
`.gitignore` and the `gitleaks` pre-commit hook protect you, but the
responsibility is yours. The dedicated guide,
[keeping data & secrets safe](10-keeping-data-and-secrets-safe.md), covers this
properly — read it before your first push.

## Connecting your project to GitHub

1. On GitHub, click **New repository**. Give it a name. **Don't** let it add a
   README or licence — your project already has those.
2. GitHub shows you a command to connect your existing project. It looks like:

   ```bash
   git remote add origin https://github.com/your-username/your-repo.git
   git push -u origin main
   ```

A **remote** is just a nickname (`origin`) for the online copy. `push` uploads
your commits to it.

## The everyday loop

Once connected, your daily rhythm adds one step to the git loop:

```bash
git add .
git commit -m "Add chart of waiting times"
git push                 # send your commits up to GitHub
```

And to bring down changes (for example, ones a teammate pushed):

```bash
git pull                 # fetch and merge the latest from GitHub
```

A good habit: **pull before you start, push when you pause.**

## Branches and pull requests

When you're working with others — or just want to keep a risky change separate —
you use a **branch**: a parallel line of work that doesn't disturb `main`.

```bash
git switch -c add-new-chart   # create and move to a new branch
# ...make commits...
git push -u origin add-new-chart
```

On GitHub you then open a **pull request** (PR): a proposal to merge your branch
into `main`. A PR is where teammates review your change, discuss it, and approve
it before it becomes part of the main project. For a first solo project you can
commit straight to `main`; branches and PRs become valuable the moment more than
one person is involved.

## Try it

If you have a GitHub account, create an empty repository, connect it with the
two commands above, and push. Refresh the GitHub page — your files, your commit
history, and your README are all there. That's your backup and your shareable
link in one.

➡️ Next: [Keeping data & secrets safe](10-keeping-data-and-secrets-safe.md)
