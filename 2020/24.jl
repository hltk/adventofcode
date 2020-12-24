movs = Dict(
    "e"  => (x, y, z) -> (x + 1, y - 1, z),
    "w"  => (x, y, z) -> (x - 1, y + 1, z),
    "se" => (x, y, z) -> (x, y - 1, z + 1),
    "sw" => (x, y, z) -> (x - 1, y, z + 1),
    "nw" => (x, y, z) -> (x, y + 1, z - 1),
    "ne" => (x, y, z) -> (x + 1, y, z - 1),
)

function neigh(p)
    x, y, z = p
    return [
        (x + 1, y - 1, z),
        (x - 1, y + 1, z),
        (x, y - 1, z + 1),
        (x - 1, y, z + 1),
        (x, y + 1, z - 1),
        (x + 1, y, z - 1),
    ]
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
        cnt(p) = sum(x ∈ alive for x in neigh(p))
        alive = union!(Set([p for p ∈ alive if 1 <= cnt(p) <= 2]), [n for p ∈ alive for n ∈ neigh(p) if cnt(n) == 2])
    end
    println(length(alive))
end

main(readlines("24.in"))
