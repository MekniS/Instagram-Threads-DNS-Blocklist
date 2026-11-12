# Instagram + Threads DNS Blocklist

AdGuard-compatible rules for Instagram and Threads, including **aggressive shared Meta API blocks**.

> **Warning:** The aggressive rules for `graph.facebook.com`, `b-graph.facebook.com`, and `edge-mqtt.facebook.com` can disrupt Facebook, Messenger, and other Meta-integrated apps. Delete these lines if you want to minimize collateral damage.

## Subscribe

After uploading this project to a public GitHub repository on its default `main` branch, the subscription URL is:

```text
https://raw.githubusercontent.com/YOUR_USERNAME/instagram-threads-dns-blocklist/main/blocklist.txt
```

Replace `YOUR_USERNAME` with your GitHub username. This is a **template**, not a live URL until published.

**AdGuard Home:** Filters → DNS blocklists → Add blocklist → Add a custom list → paste URL. Configure the refresh interval if available.

**AdGuard Private DNS:** Use Custom blocklists if your plan/dashboard supports URL subscriptions; otherwise copy the file contents into User rules. Pasted rules do not synchronize automatically.

## Repository layout

- `blocklist.txt`: subscription file, containing aggressive rules by default
- `scripts/validate.py`: checks formatting and duplicate domains
- `.github/workflows/validate.yml`: checks changes on pushes/PRs and weekly

## Updates

Edit `blocklist.txt`, commit to `main`, and the same raw URL serves the updated version. DNS clients adopt changes only after their configured refresh interval, or after a manual refresh. GitHub Actions validates list syntax **but does not automatically discover domains, update content, or test whether blocking is effective**. Review DNS query logs before adding new hosts.

## Limitations

DNS blocking cannot reliably distinguish Instagram traffic from other Meta services on shared hostnames, nor prevent bypass by VPN, alternative encrypted DNS, or mobile data. Some domains in this list are historical, lookalike or third-party domains and are not required for operation of the Instagram/Threads apps. Inclusion is not proof of current Meta ownership.

## Test

```bash
python3 scripts/validate.py
```

## Contributing

Provide the domain, observed client, date, and a redacted DNS log entry in a pull request. Do not include private IPs or device identifiers in public issues.
