# Task 06 - Process Scheduling

## About

This program is a CPU process scheduling simulator written in Go.

It takes a set of processes and calculates their:

* Completion Time
* Turnaround Time
* Waiting Time

The program also compares different scheduling methods and displays the results.

## Scheduling Algorithms

The program uses these scheduling algorithms:

### 1. FCFS (First Come First Serve)

Processes are executed in the order in which they arrive.

The process that arrives first gets executed first.

### 2. SJF (Shortest Job First)

The process with the shortest burst time is selected first from the available processes.

### 3. Priority Scheduling

The process with the highest priority is selected for execution.

### 4. Round Robin

Each process gets a fixed amount of CPU time called a **time quantum**.

If a process is not finished within its time quantum, it goes back into the queue and gets another turn later.

## Important Terms

**Arrival Time (AT)**
The time at which a process enters the ready queue.

**Burst Time (BT)**
The amount of CPU time required by a process.

**Completion Time (CT)**
The time at which a process finishes execution.

**Turnaround Time (TAT)**

```text
TAT = Completion Time - Arrival Time
```

**Waiting Time (WT)**

```text
WT = Turnaround Time - Burst Time
```

## How the Program Works

1. The user provides the process details.
2. The program stores the process information.
3. Each scheduling algorithm creates its own execution order.
4. Completion, turnaround and waiting times are calculated.
5. The results are displayed in the terminal.
6. The scheduling methods can then be compared based on their calculated values.

## Running the Program

Make sure Go is installed.

Run:

```bash
go run scheduler.go
```

If you want to format the code before running it:

```bash
gofmt -w scheduler.go
```

## Example Process

A process can contain information such as:

```text
Process ID: P1
Arrival Time: 0
Burst Time: 5
Priority: 2
```

The program uses these values to decide when the process should run and to calculate its final timings.

## What I Learned

While doing this task, I learned the basics of Go and how process scheduling works.

Some of the main concepts I used were:

* Structs
* Slices
* Functions
* Loops and conditions
* Sorting
* Copying slices
* CPU scheduling
* Waiting and turnaround time calculations
* `gofmt`

## Challenges

The main challenge was understanding how the scheduling algorithms work differently.

I also had to make sure that the processes were handled correctly when they had different arrival times and burst times.

Round Robin was another part that required some extra attention because processes can be executed multiple times before they are completed.