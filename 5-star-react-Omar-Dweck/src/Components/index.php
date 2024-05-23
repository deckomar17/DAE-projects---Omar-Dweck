<?php
require_once 'vendor/autoload.php';

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Matcher\UrlMatcher;
use Symfony\Component\Routing\RequestContext;
use Symfony\Component\Routing\RouteCollection;
use Symfony\Component\Routing\Route;

$routes = new RouteCollection();
$routes->add('add_task', new Route('/add', array(
    '_controller' => 'addTask',
)));
$routes->add('list_tasks', new Route('/', array(
    '_controller' => 'listTasks',
)));
$routes->add('delete_task', new Route('/delete/{id}', array(
    '_controller' => 'deleteTask',
    'id' => null,
)));


$context = new RequestContext();
$matcher = new UrlMatcher($routes, $context);


$request = Request::createFromGlobals();
$parameters = $matcher->match($request->getPathInfo());


switch ($parameters['_controller']) {
    case 'addTask':
        addTask($request);
        break;
    case 'listTasks':
        listTasks();
        break;
    case 'deleteTask':
        deleteTask($parameters['id']);
        break;
    default:
        $response = new Response('Not found', 404);
        $response->send();
        break;
}


function addTask(Request $request)
{


    $response = new Response('Task added', 302);
    $response->headers->set('Location', '/');
    $response->send();
}

function listTasks()
{

    $response = new Response('
        <h1>Todo List</h1>
        <ul>
            <li>Eat 1</li>
            <li>Sleep 2</li>
            <li>Reapet 3</li>
        </ul>
    
    ');
    $response->send();
}

function deleteTask($id)
{

    $response = new Response('Task deleted', 302);
    $response->headers->set('Location', '/');
    $response->send();
}
