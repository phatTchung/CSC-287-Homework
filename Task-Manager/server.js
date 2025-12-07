import express from 'express';
import expressLayouts from 'express-ejs-layouts';
import usersRouter from './routes/users.js';

// I added this line to include the tasks routes file
import tasksRouter from './routes/tasks.js';

const app = express();

app.set('view engine', 'ejs');
app.use(expressLayouts);
app.set('layout', 'layout');

app.use(express.urlencoded({ extended: true })); // body parser

app.get('/', (req, res) => res.render('home', { title: 'Home' }));

app.use('/users', usersRouter);

// I added this so the app can handle /tasks URLs
app.use('/tasks', tasksRouter);

app.listen(3000, () => console.log('Server running on http://localhost:3000'));
