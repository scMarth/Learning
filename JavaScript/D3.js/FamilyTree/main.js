// Sample data
const nodes = [
  { id: 'John' },
  { id: 'Jane' },
  { id: 'Child1' },
];

const links = [
  { source: 'John', target: 'Child1' },
  { source: 'Jane', target: 'Child1' },
];

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
