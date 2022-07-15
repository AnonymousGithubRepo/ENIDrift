**ENIDrift**
[![GitHub license][license-badge]](LICENSE)
[![Discord Chat][discord-badge]][discord]
==

**ENIDrift** is a fast and adaptive **E**nsemble system for **N**etwork **I**ntrusion **D**etection under real world **Drift**. It consists of: 1) iP2V, an incremental packet-to-vector feature extraction method; 2) Sub-classifier generation module; 3) ENIDrift update module. Compared to other network intrusion detection systems (NIDSs), we place ENIDrift under real-world drift that involves dynamically distributed network packets and well-crafted ML attacks. ENIDrift is also much faster than state-of-the-art approach, which alleviates the preasure of processing speed of network packets in real world. 

The technique design of this work is introduced in this [updated paper](https://github.com/AnonymousGithubRepo/ENIDrift/blob/main/ENIDrift.pdf). Besides, we provide the code of ENIDrift in this repo, and also open-source the first real-world drift dataset for network intrusion detection (RWDIDS'22).
## Use cases
## Key features
## Prerequisites
1. Python libraries:

2. Network packets:

## Getting started
1. Download the source code:
```sh
git clone https://github.com/AnonymousGithubRepo/ENIDrift
```

2. Run ENIDrift:
```sh
.
```

## Advanced functions
1. Model save:

2. Model load:

3. Control the speed of the release of training data:

## Documentation
See [the paper](https://github.com/AnonymousGithubRepo/ENIDrift/blob/main/ENIDrift.pdf) for details on ENIDrift concepts and configuration.

## Community & help
* Got a question? Please get in touch via [Discord][discord] or file an [issue](https://github.com/anonymousgithubrepo/enidrift/issues).
* If you see an error message or run into an issue, please make sure to create a [bug report](https://github.com/anonymousgithubrepo/enidrift/issues).

## Contribute

<!-- refs -->
[license-badge]: https://img.shields.io/github/license/anonymousgithubrepo/enidrift
[discord]: https://discord.gg/BeVM624n
[discord-badge]: https://img.shields.io/badge/chat-on%20Discord-blue
