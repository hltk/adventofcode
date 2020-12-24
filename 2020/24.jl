movs = Dict(
    "e"  => (x, y, z) -> (x + 1, y - 1, z),
    "w"  => (x, y, z) -> (x - 1, y + 1, z),
    "se" => (x, y, z) -> (x, y - 1, z + 1),
    "sw" => (x, y, z) -> (x - 1, y, z + 1),
    "nw" => (x, y, z) -> (x, y + 1, z - 1),
    "ne" => (x, y, z) -> (x + 1, y, z - 1),
)

function neigh(p::Tuple{Int, Int, Int})
    c = Tuple{Int, Int, Int}[]
    for f in values(movs)
        push!(c, f(p...))
    end
    return c
end

function main(inp)
    alive = Set()
    for l in inp
        p = (0, 0, 0)
        i = 1
        while i <= length(l)
            if l[i] == 's' || l[i] == 'n'
                mov = l[i:i+1]
                i += 2
            else
                mov = l[i:i]
                i += 1
            end
            p = movs[mov](p...)
        end
        (p ∈ alive ? pop! : push!)(alive, p)
    end
    println(length(alive))
    for t in 1:100
        function good(p)
            cnt = length([x for x in neigh(p) if x ∈ alive])
            return cnt == 2 || (p ∈ alive && cnt == 1)
        end
        totest = Iterators.flatten(neigh.(alive))
        alive = Set([p for p in totest if good(p)])
    end
    println(length(alive))
end

main(readlines("24.in"))
