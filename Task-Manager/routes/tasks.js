import express from 'express';
import {
  getTasksByUser,
  addTask,
  updateTask,
  toggleTaskCompleted,
  deleteTask,
} from '../db/taskModel.js';
import { getAllUsers } from '../db/userModel.js';

const router = express.Router();

// List tasks for a user
router.get('/user/:id', (req, res) => {
  // TODO: Implement the functionality to retrieve tasks by user (use the getTasksByUser method in taskModel.js)

  // I added this to get the user id from the URL
  const id = parseInt(req.params.id, 10);

  // I used getAllUsers() to find the matching user
  const users = getAllUsers();
  const user = users.find((u) => u.id === id);

  if (!user) return res.status(404).send('User not found');

  // I added this to get all tasks that belong to the user
  const tasks = getTasksByUser(id);

  res.render('tasks/index', { title: `Tasks for ${user.name}`, tasks, user });
});

// Add task
router.post('/add', (req, res) => {
  const { user_id, title } = req.body;
  if (!title || !user_id) return res.status(400).send('Missing fields');

  addTask(user_id, title.trim());
  res.redirect(`/tasks/user/${user_id}`);
});

// Update task (full edit: title + completed)
router.post('/update/:id', (req, res) => {
  const { id } = req.params;
  const { title, completed, user_id } = req.body;

  if (!title || !user_id) return res.status(400).send('Missing fields');

  // completed may be "on" from checkbox, so convert to boolean
  const completedBool =
    completed === 'on' || completed === '1' || completed === true;

  updateTask(id, title.trim(), completedBool);
  res.redirect(`/tasks/user/${user_id}`);
});

// Toggle completion quickly (no title change)
router.post('/toggle/:id', (req, res) => {
  const { id } = req.params;
  const { user_id } = req.body; // receive user_id to redirect back

  toggleTaskCompleted(id);
  res.redirect(`/tasks/user/${user_id}`);
});

// Delete task
router.post('/delete/:id', (req, res) => {
  // TODO: Implement the functionality to delete the specified task

  const { id } = req.params;
  const { user_id } = req.body;

  // I added this to delete the task from the database
  deleteTask(id);

  // I redirect back to the task list for the same user
  res.redirect(`/tasks/user/${user_id}`);
});

export default router;
