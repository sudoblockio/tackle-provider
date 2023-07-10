# tackle-provider

[![GitHub Release](https://img.shields.io/github/release/sudoblockio/tackle-provider.svg?style=flat)]()
![](https://github.com/sudoblockio/tackle-provider/workflows/main-tests/badge.svg?branch=main)

A [tackle](https://github.com/robcxyz/tackle-box) provider for creating new [tackle providers](https://sudoblockio.github.io/tackle/creating-providers/).

### Usage

```shell
pip install tackle
tackle sudoblockio/tackle-provider
```

Running `tackle sudoblockio/tackle-provider help`

```text
usage: tackle  [--project_slug] [--project_name] [--description] [--author_name] [--author_email] [--repo_owner] [--default_branch] [--tackle_file] [--hooks_enable] [--tests_enable]

Create a tackle provider with tests and a CI.

options:
    --project_slug [str]
    --project_name [str]
    --description [str]
    --author_name [str]
    --author_email [str]
    --repo_owner [str]
    --default_branch [str]
    --tackle_file [str]
    --hooks_enable [str]
    --tests_enable [str]
```

Running `tackle sudoblockio/tackle-provider`

```text
? Name of project slug? Actual repo name. tackle-awesome-provider
? Name of your provider? Used in README.md title. Tackle Awesome Provider
? A description of what the project is? A tackle box provider that does awesome stuff...
? What is your name? Used in README and LICENSE Donald Duck
? What is your email? Blank to leave out. duckman5000@gmail.com
? What is your github / org name? dduck43
? What is going to be your default branch name?
❯ main
  master
? license_type >>>
❯ Apache 2.0
  MIT
  GPL Version 3
  BSD Version 3
  Closed source
? What year to end the license? (current year is fine) 2022
? What type of default tackle file do you want to start with?
❯ Code generation boiler plate - full project
  Declarative CLI
  No tackle file - provider is just for hooks
? Do you want to setup hooks? Yes
? What is your hook type? (Used to call hook) stuff
? What is the class name? StuffHook
? Do you want to generate tests? Yes
? Do you want to use tox? Yes
? Do you want to generate continuous integration scripts? Yes
? What platforms to test against?
  ◉ ubuntu
  ◉ macos
❯ ◉ windows
? Which python versions to test against? Will run in matrix.
❯ ◉ 3.7
  ◉ 3.8
  ◉ 3.9
  ◉ 3.10
? Do you want to use Foresight for test telemetry? Yes
```

### TTD

- [ ] Make github action into provider
- [ ] Make badges into provider
- [ ] Modularize the calls and improve testing
- [ ] Use naming provider?

### License

Apache 2.0
