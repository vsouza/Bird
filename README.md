#Bird 

iOS Push Notifications.
<img src="https://raw.githubusercontent.com/vsouza/Bird/master/icon.png" align="right">  

Bird is a project to facilitate the integration of push messages on any system. Enjoy and send your pull request.

## How To use

You can use the Bird in the way that suits you in any programming language or even within your project in Python.

__In PHP:__

```php
$cmd = 'python apns.py --badge 1 --message "Test message" --sound "default"';
exec($cmd);
```
__In Command line__

```shell
python apns.py --badge  1 --message "Test message" --sound "default"
```

## Reference

 * [APNS](https://developer.apple.com/library/IOs/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html)
 

## License

[MIT License](http://vsouza.mit-license.org/) © Vinicius Souza
