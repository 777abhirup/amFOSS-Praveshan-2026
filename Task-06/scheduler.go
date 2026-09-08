package main

import (
	"fmt"
	"sort"
)

type Process struct {
	ID                              string
	Arrival, Burst, Priority        int
	Completion, Turnaround, Waiting int
}

func clone(ps []Process) []Process { q := make([]Process, len(ps)); copy(q, ps); return q }

func fcfs(ps []Process) []Process {
	sort.Slice(ps, func(i, j int) bool { return ps[i].Arrival < ps[j].Arrival })
	t := 0
	for i := range ps {
		if t < ps[i].Arrival {
			t = ps[i].Arrival
		}
		t += ps[i].Burst
		ps[i].Completion = t
		ps[i].Turnaround = t - ps[i].Arrival
		ps[i].Waiting = ps[i].Turnaround - ps[i].Burst
	}
	return ps
}

func sjf(ps []Process) []Process {
	done := 0
	t := 0
	for done < len(ps) {
		idx := -1
		for i, p := range ps {
			if p.Completion == 0 && p.Arrival <= t && (idx < 0 || p.Burst < ps[idx].Burst) {
				idx = i
			}
		}
		if idx < 0 {
			t++
			continue
		}
		t += ps[idx].Burst
		ps[idx].Completion = t
		ps[idx].Turnaround = t - ps[idx].Arrival
		ps[idx].Waiting = ps[idx].Turnaround - ps[idx].Burst
		done++
	}
	return ps
}

func priority(ps []Process) []Process {
	done := 0
	t := 0
	for done < len(ps) {
		idx := -1
		for i, p := range ps {
			if p.Completion == 0 && p.Arrival <= t && (idx < 0 || p.Priority < ps[idx].Priority) {
				idx = i
			}
		}
		if idx < 0 {
			t++
			continue
		}
		t += ps[idx].Burst
		ps[idx].Completion = t
		ps[idx].Turnaround = t - ps[idx].Arrival
		ps[idx].Waiting = ps[idx].Turnaround - ps[idx].Burst
		done++
	}
	return ps
}

func main() {
	base := []Process{{ID: "P1", Arrival: 0, Burst: 5, Priority: 2}, {ID: "P2", Arrival: 1, Burst: 3, Priority: 1}, {ID: "P3", Arrival: 2, Burst: 8, Priority: 3}, {ID: "P4", Arrival: 3, Burst: 2, Priority: 2}}
	algos := []struct {
		name string
		fn   func([]Process) []Process
	}{{"FCFS", fcfs}, {"SJF", sjf}, {"Priority", priority}}
	fmt.Println("CPU Scheduling Simulator")
	for _, a := range algos {
		r := a.fn(clone(base))
		var tw, tt int
		fmt.Println("\n", a.name)
		fmt.Println("PID Arrival Burst Priority Completion Turnaround Waiting")
		for _, p := range r {
			fmt.Printf("%s %d %d %d %d %d %d\n", p.ID, p.Arrival, p.Burst, p.Priority, p.Completion, p.Turnaround, p.Waiting)
			tw += p.Waiting
			tt += p.Turnaround
		}
		fmt.Printf("Average Waiting: %.2f | Average Turnaround: %.2f\n", float64(tw)/float64(len(r)), float64(tt)/float64(len(r)))
	}
}
