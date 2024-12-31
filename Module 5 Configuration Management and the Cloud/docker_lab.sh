gcloud auth list
gcloud config list project
docker run hello-world
docker images #find all images loaded into docker
docker run hello-world #run docker project
docker ps
docker ps -a #check all docker processes including stopped ones
mkdir test && cd test
cat > Dockerfile <<EOF
# Use an official Node runtime as the parent image
FROM node:lts

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Make the container's port 80 available to the outside world
EXPOSE 80

# Run app.js using node when the container launches
CMD ["node", "app.js"]
EOF
#file above to make docter file 
cat > app.js <<EOF
const http = require('http');

const hostname = '0.0.0.0';
const port = 80;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

server.listen(port, hostname, () => {
    console.log('Server running at http://%s:%s/', hostname, port);
});

process.on('SIGINT', function() {
    console.log('Caught interrupt signal and will exit');
    process.exit();
});
EOF
#file above to create the node app
docker build -t node-app:0.1 . #build node app in current dir
docker images # run to see new node app
docker run -p 4000:80 --name my-app node-app:0.1 # run the app
curl http://localhost:4000 #see the app running
docker stop my-app && docker rm my-app # stop first app and remove it
docker run -p 4000:80 --name my-app -d node-app:0.1
docker ps
#start container in backgroup ^ 
docker logs 9af #pull logs for app
cd test
sudo nano app.js 
: '
const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Welcome to Cloud\n');
});
'
#code above to edit app
docker build -t node-app:0.2 .
docker run -p 8080:80 --name my-app-2 -d node-app:0.2
docker ps
curl http://localhost:8080 #see new container
curl http://localhost:4000 #first container
docker logs -f bf9 #grab logs from second container
docker exec -it bf9 bash #start bash in container
docker inspect bf9 #inspect metadata
: '

[
    {
        "Id": "bf96f5439e186d026facb5592bb87cf05ce653523ad770ac46741241ea74a315",
        "Created": "2024-12-13T15:14:27.863471026Z",
        "Path": "docker-entrypoint.sh",
        "Args": [
            "node",
            "app.js"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 2073,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2024-12-13T15:14:28.010183956Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:f330c0aace7c15a8396c760afc9873569222895930e29a553de622fc80af39d1",
        "ResolvConfPath": "/var/lib/docker/containers/bf96f5439e186d026facb5592bb87cf05ce653523ad770ac46741241ea74a315/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/bf96f5439e186d026facb5592bb87cf05ce653523ad770ac46741241ea74a315/hostname",
        "HostsPath": "/var/lib/docker/containers/bf96f5439e186d026facb5592bb87cf05ce653523ad770ac46741241ea74a315/hosts",
        "LogPath": "/var/lib/docker/containers/bf96f5439e186d026facb5592bb87cf05ce653523ad770ac46741241ea74a315/bf96f5439e186d026facb5592bb87cf05ce653523ad770ac46741241ea74a315-json.log",
        "Name": "/my-app-2",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "bridge",
            "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "8080"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                14,
                235
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": [],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/51f6d50d825633eed3d891649be2899656560993f01b476e253599748fec6eef-init/diff:/var/lib/docker/overlay2/2jfj9zfi6k0509guyfvmv2xuy/diff:/var/lib/docker/overlay2/weq08e7jarflplc5ehh51wtu6/diff:/var/lib/docker/overlay2/a7601ada2211a97ad11335b4042c43db9276b64fbafb7f86b39f7bba0e8eb1ec/diff:/var/lib/docker/overlay2/d2ab72c0d1a758864b327601dbe156c18cc9ae5b6b82fb14412e6faec09b76af/diff:/var/lib/docker/overlay2/b42fcf84b7a9fa120ad396d78f6795bc128b67a83b0c2563923e3d62b2238fe6/diff:/var/lib/docker/overlay2/439491c9fbf7b487083f45e5af8611fcb47508a12b726641469af3dfe80aeff6/diff:/var/lib/docker/overlay2/234d6b8b1ef078692ee32c34194ab632a43a27ea6d64c09a5d0f5717b49ea4df/diff:/var/lib/docker/overlay2/5b20dc5423f07e6abfa1dde61d8685bf64749a69ddf08ba2dd14ba0e450118d0/diff:/var/lib/docker/overlay2/ab77e8598af0cf3f202d5b4c90d22befd3cc4fc541cf66f5d85dcf9db4285ec2/diff:/var/lib/docker/overlay2/24147475495aa942e4e7439cea7ac1a41bcdda5bc76ece7a146744867cb352fd/diff",
                "MergedDir": "/var/lib/docker/overlay2/51f6d50d825633eed3d891649be2899656560993f01b476e253599748fec6eef/merged",
                "UpperDir": "/var/lib/docker/overlay2/51f6d50d825633eed3d891649be2899656560993f01b476e253599748fec6eef/diff",
                "WorkDir": "/var/lib/docker/overlay2/51f6d50d825633eed3d891649be2899656560993f01b476e253599748fec6eef/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "bf96f5439e18",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NODE_VERSION=22.12.0",
                "YARN_VERSION=1.22.22"
            ],
            "Cmd": [
                "node",
                "app.js"
            ],
            "Image": "node-app:0.2",
            "Volumes": null,
            "WorkingDir": "/app",
            "Entrypoint": [
                "docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "eb8f99a45b4439ba67ef779e04b1a731bde30d7f84afe14600a83afb94c084b3",
            "SandboxKey": "/var/run/docker/netns/eb8f99a45b44",
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "8080"
                    }
                ]
            },
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "560d00246dc87d8f1f31cdc81cd98ec26e0d01263b9055e5555b42cdc3087b8a",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.3",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:03",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "MacAddress": "02:42:ac:11:00:03",
                    "DriverOpts": null,
                    "NetworkID": "2660bbe934bba1070c96bed1de017b17e82f950964d649b84d4dfb6f4716bede",
                    "EndpointID": "560d00246dc87d8f1f31cdc81cd98ec26e0d01263b9055e5555b42cdc3087b8a",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        }
    }
]

'
#said metadata above
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' bf9 #grab ip
gcloud auth configure-docker us-east1-docker.pkg.dev #authenticate the docker repos in us-east1
export PROJECT_ID=$(gcloud config get-value project)
cd ~/test  #set project id and cd to the dockerfile dir
docker build -t us-east1-docker.pkg.dev/$PROJECT_ID/my-repository/node-app:0.2 . #tag the node app
docker images #check to make sure it worked
: '

REPOSITORY                                                                    TAG       IMAGE ID       CREATED          SIZE
node-app                                                                      0.2       f330c0aace7c   8 minutes ago    1.12GB
us-east1-docker.pkg.dev/qwiklabs-gcp-01-f62a6877d67c/my-repository/node-app   0.2       f330c0aace7c   8 minutes ago    1.12GB
node-app                                                                      0.1       a1fbdae34522   18 minutes ago   1.12GB
hello-world                                                                   latest    d2c94e258dcb   19 months ago    13.3kB

'
docker push us-east1-docker.pkg.dev/$PROJECT_ID/my-repository/node-app:0.2
: '
The push refers to repository [us-east1-docker.pkg.dev/qwiklabs-gcp-01-f62a6877d67c/my-repository/node-app]
b19a82a15f28: Pushed 
c4bad84e360a: Pushed 
e0dba9f2a2ef: Pushed 
b37454b23b8f: Pushed 
fb6c888e3ccc: Pushed 
952f5ee3867b: Pushed 
0aeeeb7c293d: Pushed 
c81d4fdb67fc: Pushed 
0e82d78b3ea1: Pushed 
301c1bb42cc0: Pushed 
0.2: digest: sha256:d39961d38d820f65203aff0b80254a7ea4527bd8b0e088324a3a6e63eab7ffed size: 2417

'
#output from push
docker stop $(docker ps -q)
docker rm $(docker ps -aq) #remove all containers
docker rmi us-east1-docker.pkg.dev/$PROJECT_ID/my-repository/node-app:0.2
docker rmi -f $(docker images -aq) # remove remaining images
docker images
docker pull us-east1-docker.pkg.dev/$PROJECT_ID/my-repository/node-app:0.2 # pull image from artifact registry 
docker run -p 4000:80 -d us-east1-docker.pkg.dev/$PROJECT_ID/my-repository/node-app:0.2 # run the app
curl http://localhost:4000 # make sure it's running