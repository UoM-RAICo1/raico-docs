# RAICo1 Documentation

To use this repo first clone it to your local machine.

```bash
git clone git@github.com:UoM-RAICo1/raico-docs.git
```

Then install the dependencies using the following command:

```bash
pip install -r requirements.txt
```


## Building the documentation

To build the documentation, run the following command:

```bash
cd docs
make html
```

The documentation will be built in the `docs/build/html` directory.

## Viewing the documentation

To view the documentation, open the `index.html` file in the `docs/build/html` directory in a web browser.

```bash
cd docs/build/html
open index.html
```

## Making changes

First create a new branch to make changes to the documentation. The branch name can be your name which will be used to identify the changes you made.

```bash
git checkout -b <branch-name>
```

Then make changes to the documentation.
To make changes to the documentation, edit the `.rst` files in the `docs/source` directory. 

## Pushing changes

To push changes to the repository, first commit the changes.

```bash
git add .
git commit -m "Commit message"
```

Then push the changes to the repository.

```bash
git push origin <branch-name>
```

Finally, create a pull request on GitHub to merge the changes into the `main` branch.

## Documentation structure

The documentation is structured as follows:

```
RAICo1 Documentation
├─ Introduction
│  ├─ Overview
│  ├─ Objectives
├─ Using RAICo1
│  ├─ Safety & Security
│  ├─ ...
├─ Robots
│  ├─ ARMs
│  │  ├─ KuKA LBR iiwa
│  │  ├─ Kinova Gen3
│  |  ├─ Alpha 5
│  |  ├─ Unitree Z1
│  |  ├─ ...
│  ├─ UAVs
│  │  ├─ ...
│  ├─ UGVs
│  │  ├─ ...
|  ├─ Humanoids
│  │  ├─ Unitree H1
│  │  ├─ Pepper
│  |  ├─ ...
|  ├─ Quadrupeds
│  │  ├─ Unitree A1
│  │  ├─ Unitree Go1
│  |  ├─ ...
|  ├─ Mobile Robots
│  │  ├─ AgileX Scout Mini
│  │  ├─ AgileX Scout 2
│  |  ├─ AgileX Tracer
│  |  ├─ Husarion ROSbot 2 PRO
│  |  ├─ Vega/Lyra
│  |  ├─ ...
├─ Infrastructure
│  ├─ Sensors
│  │  ├─ Cameras
│  │  | ├─ RGB
|  |  | | ├─ 
│  │  | ├─ RGBD
|  |  | | ├─ 
│  │  | ├─ Depth
|  |  | | ├─ Vacons
│  │  ├─ LiDARs
│  │  | ├─ Oster
│  │  | ├─ Velodyne
│  │  ├─ ...
│  ├─ Actuators
│  │  ├─ Motors
│  │  ├─ Servos
│  │  ├─ ...
│  ├─ Radios
│  │  ├─ ...
│  ├─ Batteries
│  │  ├─ ...
│  ├─ Vertual Reality
│  │  ├─ ...
```






