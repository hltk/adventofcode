function main(inp)
    inp = split(inp, "")
    inp = parse.(Int, inp)
    append!(inp, collect(maximum(inp)+1:10^6))
    nxt = [-1 for x in inp]
    max = maximum(inp)
    for (i, a) in enumerate(inp)
        nxt[a] = inp[begin + i % length(inp)]
    end
    cur = inp[1]
    for i in 1:10^7
        vals = Int[]
        orig = cur
        for i in 1:3
            cur = nxt[cur]
            push!(vals, cur)
        end
        cur = nxt[cur]
        nxt[orig] = cur
        dest = orig
        while dest == orig || dest in vals
            dest -= 1
            if dest < 1
                dest = max
            end
        end
        nxt[vals[3]] = nxt[dest]
        nxt[vals[2]] = vals[3]
        nxt[vals[1]] = vals[2]
        nxt[dest] = vals[1]
    end
    println(nxt[1] * nxt[nxt[1]])
end

main("156794823")
