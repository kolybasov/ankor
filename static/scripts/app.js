// used to close notifications, modals, etc
const deleteParentBox = (evt) => {
  const notificationsBox = event.target.closest('section.notifications');
  notificationsBox.parentNode.removeChild(notificationsBox);
};

// perform action with link short/delete/etc
const linkAction = (evt, action) => {
  const actionInput = evt.target.closest('form').querySelector('input[name="action"]');
  actionInput.value = action;
}
