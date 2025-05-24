// Force-directed graph



const fam_dat = [
    /* OBJECTID, Name, Mother ID, Father ID */
    {'OBJECTID': 1, 'NAME': 'John', 'M_ID': null, 'F_ID': null},
    {'OBJECTID': 2, 'NAME': 'Jane', 'M_ID': null, 'F_ID': null},
    {'OBJECTID': 3, 'NAME': 'Child1', 'M_ID': 2, 'F_ID': 1},
    {'OBJECTID': 4, 'NAME': 'Child2', 'M_ID': 2, 'F_ID': 1},
];


// Sample data
// const nodes = [
//     { id: 'John' },
//     { id: 'Jane' },
//     { id: 'Child1' },
// ];


// Create a map from OBJECTID to NAME (to reference parents by ID)
const idToName = {};
fam_dat.forEach(person => {
  idToName[person.OBJECTID] = person.NAME;
});

// create nodes
const nodes = fam_dat.map(person => ({
    id: person.NAME
}));


// create links
const links = [];

fam_dat.forEach(person => {
    if (person.M_ID !== null) {
      links.push({
        source: idToName[person.M_ID],
        target: person.NAME
      });
    }
    if (person.F_ID !== null) {
      links.push({
        source: idToName[person.F_ID],
        target: person.NAME
      });
    }
});

// Select the SVG
const svg = d3.select('svg');
const width = window.innerWidth;
const height = window.innerHeight;

// Create simulation
const simulation = d3.forceSimulation(nodes)
.force('link', d3.forceLink(links).id(d => d.id).distance(150))
.force('charge', d3.forceManyBody().strength(-400))
.force('center', d3.forceCenter(width / 2, height / 2));

// Draw links (lines between nodes)
const link = svg.append('g')
.attr('stroke', '#aaa')
.selectAll('line')
.data(links)
.join('line')
.attr('class', 'link');

// Draw nodes (circles + labels)
const node = svg.append('g')
.selectAll('g')
.data(nodes)
.join('g')
.attr('class', 'node');

node.append('circle')
.attr('r', 20)
.attr('fill', 'steelblue');

node.append('text')
.text(d => d.id)
.attr('dy', 4);

// Update positions on each tick
simulation.on('tick', () => {
link
    .attr('x1', d => d.source.x)
    .attr('y1', d => d.source.y)
    .attr('x2', d => d.target.x)
    .attr('y2', d => d.target.y);

node
    .attr('transform', d => `translate(${d.x},${d.y})`);
});
