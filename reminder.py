from datetime import datetime


def github_reminder():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=" * 50)
    print(f"  GitHub Profile Reminder  [{now}]")
    print("=" * 50)
    print("Hey! Time to check and contribute to your GitHub profile.")
    print()
    print("Here are a few things you can do:")
    print("  - Review and merge open pull requests")
    print("  - Close or comment on open issues")
    print("  - Push new commits to keep your contribution graph active")
    print("  - Update your profile README with recent work")
    print("  - Star or fork interesting repositories")
    print("  - Review your pinned repositories and keep them up to date")
    print()
    print("Happy coding! Every contribution counts.")
    print("=" * 50)


if __name__ == "__main__":
    github_reminder()
